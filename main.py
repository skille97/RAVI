from flask import *
app = Flask(__name__)



@app.route("/")
def main():
    return render_template('index.html')

@app.route('/changeCell/', methods=['POST'])
def changeCell():
    cell=request.form['cell']
    data=request.form['data']


@app.route('/moveRow/', methods=['POST'])
def moveRow():
    axis=request.form['axis']
    start=request.form['from']
    to=request.form['to']

    




if __name__ == "__main__":
    app.run(debug=True)

