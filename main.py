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

#Add entry with the name, comments, components and PCB as values
def addEntry(name, comments, components, PCB):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    #Hold on to your butts, this is a long one.
    c.execute("INSERT INTO tasks (position, name, comments, components, PCB, visible) VALUES((SELECT IFNULL(MAX(position), 0) + 1 FROM tasks), ?, ?, ?, ?, ?)", [name, comments, components, PCB, 1])
    db.commit()
    db.close()

#Update the cell with the ID row. Then the column "column" is set to newValue. 
def updateCell(row, column, newValue):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    c.execute("UPDATE tasks SET " + column + " = ? WHERE id=?", [newValue, row])
    db.commit()
    db.close()

@app.route('/updateRow/', methods=['POST'])
def updateRow():
    row = request.json['id']
    column = request.json['column']
    newValue = request.json['newValue']
    headers = ["id", "name", "comments", "components", "PCB"]
    column = headers[int(column)]
    updateCell(row, column, newValue)
    # retrnes a sringe ingore
    return "lol"


def getTasks():
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    body = []
    for row in cursor.execute("SELECT * FROM tasks WHERE visible=1 ORDER BY position"):
        body.append([row[0], row[2], row[5], row[4], row[3]])
    return body



@app.route("/")
def main():
    headers = ["ID", "Navn", "PCB", "Components", "Kommentarer"]
    return render_template('index.html', headers=headers, body=getTasks())

@app.route('/addRow/', methods=['POST'])
def addRow():
    text = request.json['text']
    addEntry(text, "", "", "")
    print(text)
    return "true"


if __name__ == "__main__":
    dbInit()
    app.run(debug=True, host="0.0.0.0")
