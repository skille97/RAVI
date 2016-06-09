from flask import *
app = Flask(__name__)

@app.route("/")
def hello():
    headers = ["Header1", "Header2", "Header3"]
    body = [["Body", "Body", "Body"], ["Body", "Body", "Body"]]
    return render_template('index.html', headers=headers, body=body)

if __name__ == "__main__":
    app.run(debug=True)

