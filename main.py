#!/usr/bin/env python3
from flask import *
import sqlite3
import re
import atexit
import csv
import sys, os


#Define working directory. Defualts to current
if len(sys.argv) > 1:
    os.chdir(sys.argv[1])
    print("Working directory set to " + os.getcwd())
else:
    print("No working directory specified, using current.")


#BOM stuff
from werkzeug.utils import secure_filename
from BOM.bom import conveter
import shutil

#for tempfiles
UPLOAD_FOLDER = './upload/'
if not os.path.isdir(UPLOAD_FOLDER):
	print(" * Could not find " + UPLOAD_FOLDER + ". Making new")
	os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__, root_path=os.getcwd())
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db_name = "RAVI.db"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Header configuration start
#Database headers without primary headers; id, position, name and visible. Order is not important.
#                    3        4          5          6           7           8            9         10       11         12
databaseHeader = ["data", "stencil", "program", "montage", "delivery", "comments", "components", "PCB", "customer", "count"] #Changing this requires a new database

#Order and names the headers on website should have, order is important. Note that id, position, name and visible should be present here.
displayHeaders = ["ID", "Kunde", "Projekt", "Antal", "Data", "Stencil", "Program", "Montage", "Levering", "PCB", "Komponenter", "Kommentarer", "Komplet"]

#Order the different data should be displayed where number represents number in databaseHeaderWithIPNV. Should corrospond to displayHea
order = [0] + [11, 2, 12, 3, 4, 5, 6, 7, 10, 9, 8] #Komplet vil altid være sidst og skal ikke skrives med. Id skal være i starten og må derfor ikke flyttes

#Header confiduration end

databaseHeaderWithIPNV = ["id", "position", "name"] + databaseHeader + ["visible"]
databaseHeaderOrder = []
for i in order:
	databaseHeaderOrder.append(databaseHeaderWithIPNV[i])


def getDisplayOrder(row):
	#Order the different data should be displayed where number represents number in databaseHeader. Should corrospond to displayHeaders
	returnList = []
	for i in order:
		returnList.append(row[i])
	return returnList


def insertDBheader(DBheaders):
	text = ""
	for header in DBheaders:
		text = text + header + " TEXT, "
	return text

def makeExecuteSpaces(amount, string):
	text = ""
	for i in range(0, amount):
		text = text + ", " + string
	return text

#TODO: Database versioning
def dbInit():
	db = sqlite3.connect(db_name)
	db.execute("CREATE TABLE IF NOT EXISTS tasks ( id INTEGER PRIMARY KEY NOT NULL, position INTEGER NOT NULL, name TEXT, " + insertDBheader(databaseHeader) + " visible INTEGER)")
	db.execute("CREATE TABLE IF NOT EXISTS colours ( id INTEGER PRIMARY KEY NOT NULL, position INTEGER NOT NULL, name TEXT, " + insertDBheader(databaseHeader) + " visible INTEGER)")

	db.close()

#Add entry with the name, comments, components and PCB as values
def addEntry(name):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    #Hold on to your butts, this is a long one.
    c.execute("INSERT INTO tasks (position, name, " + ', '.join(databaseHeader) + ", visible) VALUES((SELECT IFNULL(MAX(position), 0) + 1 FROM tasks), ?" + makeExecuteSpaces(len(databaseHeader), "''") + ", 1)", [name])
    c.execute("INSERT INTO colours (position, name, " + ', '.join(databaseHeader) + ", visible) VALUES((SELECT IFNULL(MAX(position), 0) + 1 FROM colours)" + makeExecuteSpaces(len(databaseHeader) + 1, "' '") + ", 1)")
    db.commit()
    db.close()

#Update the cell with the ID row. Then the column "column" is set to newValue.
def updateCell(row, column, newValue):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    #Remove anything that isn't a character from a-Z from the column value with a regex. This should help against SQL injection.
    column = re.sub("[^a-zA-Z]","", column)
    c.execute("UPDATE tasks SET " + column + " = ? WHERE id=?", [newValue, row])
    db.commit()
    db.close()

@app.route('/updateRow/', methods=['POST'])
def updateRow():
	row = request.json['id']
	column = request.json['column']
	newValue = request.json['newValue']
	column = databaseHeaderOrder[int(column)]
	updateCell(row, column, newValue)
	# retrnes a sringe ingore
	return "lol"

@app.route('/hideRow/', methods=['POST'])
def hideRow():
    row = request.json['id']
    updateCell(row, "visible", request.json['visible'])
    #Updates the colour database
    db = sqlite3.connect(db_name)
    c = db.cursor()
    c.execute("UPDATE colours SET " + "visible" + " = ? WHERE id=?", [request.json['visible'], row])
    db.commit()
    db.close()
    return "Row number" + str(row) + " hidden"

def getTasks():
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    body = []
    for row in cursor.execute("SELECT * FROM tasks WHERE visible=1 ORDER BY position"):
        body.append(getDisplayOrder(row))

    return body

def getColours():
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    colours = []
    for row in cursor.execute("SELECT * FROM colours WHERE visible=1 ORDER BY position"):
        colours.append(getDisplayOrder(row))
    return colours

def getHiddenTasks():
	db = sqlite3.connect(db_name)
	cursor = db.cursor()
	body = []
	hiddenStates = []
	for row in cursor.execute("SELECT * FROM tasks ORDER BY position"):
		try:
			body.append(getDisplayOrder(row))
			hiddenStates.append(row[len(databaseHeaderWithIPNV)-1])
		except:
			print("error in getting hidden tasks")
	return [body, hiddenStates]


def getHiddenColours():
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    colours = []
    for row in cursor.execute("SELECT * FROM colours ORDER BY position"):
        colours.append(getDisplayOrder(row))
    return colours

@app.route("/")
def main():
    return render_template('index.html', headers=displayHeaders, body=getTasks(), colours=getColours(), hiddenStates=[], link="/hidden/", isHidden=False)

@app.route("/hidden/")
def hidden():
	tasks = getHiddenTasks()
	return render_template('index.html', headers=displayHeaders, body=tasks[0], colours=getHiddenColours(), hiddenStates=tasks[1],  link="/", isHidden=True)

@app.route('/addRow/', methods=['POST'])
def addRow():
    text = request.json['text']
    addEntry(text)
    return "true"

@app.route('/updateColour/', methods=['POST'])
def updateColour():
    column = databaseHeaderOrder[int(request.json['column'])]
    db = sqlite3.connect(db_name)
    c = db.cursor()
    c.execute("UPDATE colours SET " + column + " = ? WHERE id=?", [request.json['colour'], str(request.json['row'])])
    db.commit()
    db.close()
    return "true"


@app.route('/csv')
def toCsv():
	db = sqlite3.connect(db_name)
	c = db.cursor()
	body = []
	for row in c.execute("SELECT * FROM tasks ORDER BY position"):
		try:
			body.append([row[0], row[11], row[2], row[12], row[3], row[4], row[5], row[6], row[7], row[10], row[9], row[8], row[13]])
		except:
			print("error in converting to csv")
	with open("upload/out.csv", "w", newline='') as csv_file:              # Python 2 version
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(displayHeaders) # write headers
		csv_writer.writerows(body)
	return send_file("upload/out.csv", as_attachment=True)

@app.route('/bom/', methods=['GET', 'POST'])
def upload_file():
    #Check if there is a request
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            #Run the converter
            conveter(UPLOAD_FOLDER + file.filename);
            #Send converted file back to user
            return send_file(UPLOAD_FOLDER + file.filename + ".csv", as_attachment=True)
    #If no file is uploaded send bom html upload site
    return render_template('bom.html')




if __name__ == "__main__":
    dbInit()
    rootPath = os.getcwd()
    app.run(debug=False, host="0.0.0.0")
