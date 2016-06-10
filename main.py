#!/usr/bin/env python3
from flask import *
import sqlite3
app = Flask(__name__)

db_name = "RAVI.db"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#TODO: Database versioning
def dbInit():
    db = sqlite3.connect(db_name)
    db.execute("""CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY NOT NULL,
                position INTEGER NOT NULL,
                name TEXT,
                comments TEXT,
                components TEXT,
                PCB TEXT,
                visible INTEGER
                )
               """)
    db.close()

def addEntry(name, comments, components, PCB):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    c.execute("INSERT INTO tasks (position, name, comments, components, PCB, visible) VALUES((SELECT IFNULL(MAX(position), 0) + 1 FROM tasks), ?, ?, ?, ?, ?)", [name, comments, components, PCB, 1])
    db.commit()
    db.close()

def getTasks():
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    body = []
    for row in cursor.execute("SELECT * FROM tasks WHERE visible=1 ORDER BY position"):
        body.append([row[0], row[2], row[3], row[3], row[4]])
    return body



@app.route("/")
def main():
    headers = ["ID", "Navn", "Kommentarer", "Components", "PCB"]
    body = getTasks()
    return render_template('index.html', headers=headers, body=body)

@app.route('/changeCell/', methods=['POST'])
def changeCell():
    cell=request.json['cell']
    data=request.json['data']
    print(cell + "     " + data)
    return "true"


@app.route('/moveRow/', methods=['POST'])
def moveRow():
    #Axis bliver givet i x og y
    axis=request.json['axis']
    row=request.json['row']
    #Direc vil være -1 hvis det er ned eller til venstre. og direc vil være 1 hvis det er up eller højre
    direc=request.json['direc']
    print(axis + "     " + str(row) + "     " + direc)
    return "True"


@app.route('/addRow/', methods=['POST'])
def addRow():
    #Axis bliver givet i x og y, og ja jeg tjækker før det bliver sendt
    axis=request.json['axis']
    name=request.json['name']
    print(axis + "     " + name)
    return "true"


if __name__ == "__main__":
    dbInit()
    app.run(debug=True, host="0.0.0.0")
