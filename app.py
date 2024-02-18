from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def start():
    return 'Hello'

@app.route('/file')
def returnTemp():
    return render_template('index.html')

