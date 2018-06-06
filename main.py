from flask import Flask
from testpyauto import TestPyAuto

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home Page for Pyautogui Test'


@app.route('/testpyauto/start')
def start():
    testpy = TestPyAuto()
    testpy.startpyauto()
    return 'Start Application'
