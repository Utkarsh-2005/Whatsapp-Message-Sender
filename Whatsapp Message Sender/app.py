from flask import Flask, request, render_template
from pymongo import MongoClient
import send_message

client = MongoClient(port=27017)
db = client.messages

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/data', methods=["GET", "POST"])
def data():
    data = {}
    if request.method == "POST":
        data['Message'] = request.form['message']
        data['Phone'] = request.form['phone']
        data['Time'] = request.form['time']
        db.messages.insert_one(data) 
        send_message.message()
    return timer()
@app.route('/timer')
def timer():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

