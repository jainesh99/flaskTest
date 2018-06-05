from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page for Pyautogui Test'

@app.route('/start')
def start():
    return 'Start Application'