#!/usr/bin/env python3
from flask import *
app = Flask(__name__)


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
    return "true"


@app.route('/addRow/', methods=['POST'])
def addRow():
    #Axis bliver givet i x og y, og ja jeg tjækker før det bliver sendt
    axis=request.json['axis']
    name=request.json['name']
    print(axis + "     " + name)
    return "true"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
