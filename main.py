#!/usr/bin/env python3
from flask import *
import sqlite3
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def dbinet():
    db = sqlite3.connect("RAVI.db")
    db.execute("""CREATE TABLE opgaver (
                id int,
                name text
                )
               """)

@app.route("/")
def main():
    headers = ["Header1", "Header2", "Header3"]
    body = [["Body", "Body", "Body"], ["Body", "Body", "Body"]]
    return render_template('index.html', headers=headers, body=body)

@app.route('/changeCell/', methods=['POST'])
def changeCell():
    cell=request.form['cell']
    data=request.form['data']
    return 1


@app.route('/moveRow/', methods=['POST'])
def moveRow():
    axis=request.form['axis']
    start=request.form['from']
    to=request.form['to']
    return 1


@app.route('/addRow/', methods=['POST'])
def addRow():
    axis=request.form['axis']
    number=request.form['number']
    return 1



if __name__ == "__main__":
    dbinet()
    app.run(debug=True, host="0.0.0.0")





