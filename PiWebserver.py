from flask import Flask, render_template, request
from multiprocessing import Process
from LEDS import LED
import sys
import time

app = Flask(__name__)

LEDS = LED('hej med dig')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/setPattern', methods=['POST'])
def setPattern():
    try:
        req_Body = request.form
        string = req_Body['new_Message']
        LEDS.startLights()
        LEDS.setPattern(string)
        return "OK"
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


if __name__ == '__main__':
    app.run()

