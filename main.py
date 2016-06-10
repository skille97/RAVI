#!/usr/bin/env python3
from flask import *
import time
app = Flask(__name__)


#Logging stuff
fl = open('log', 'a')
def log(msg):
    fl.write("(" + time.strftime("%c") + ")" + msg + "\n")



log("Starting server")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route("/")
def main():
    headers = ["Header1", "Header2", "Header3"]
    body = [["Body", "Body", "Body"], ["Body", "Body", "Body"]]
    return render_template('index.html', headers=headers, body=body)

@app.route('/changeCell/', methods=['POST'])
def changeCell():
    cell=request.form['cell']
    data=request.form['data']
    log("Ip: " + request.remote_addr + " changed " + cell + " to " + data)
    return 1


@app.route('/moveRow/', methods=['POST'])
def moveRow():
    axis=request.form['axis']
    start=request.form['from']
    to=request.form['to']
    log("Ip: " + request.remote_addr + " moved row " + start + " to " + to + " at axis " + axis)
    return 1


@app.route('/addRow/', methods=['POST'])
def addRow():
    axis=request.form['axis']
    number=request.form['number']
    log("Ip: " + request.remote_addr + " added row" + number + " at axis " + axis)
    return 1



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")





