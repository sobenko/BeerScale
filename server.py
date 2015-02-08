from flask import Flask
from flask import render_template, send_from_directory

import threading
import serial
import time

app = Flask(__name__)

loadA = 0.0
loadB = 55.0

keg_data = {
    0: {
        'analogA': 22.91,
        'analogB': 415.30
    },
    1: {
        'analogA': 11,
        'analogB': 387.60
    }
}

# This is map of keg weights by number -> weight, the tread writes to this
kegs = {
    0: 0,
    1: 0
}

def maprange(s, analogvalA, analogvalB):
    return loadA + ((s - analogvalA) * (loadB - loadA) / (analogvalB - analogvalA))

# 128 oz in a gallon
# http://www.brewangels.com/Beerformation/Weight.html
# Light Lager with a FG of 1.008: 8.345 x 1.008 = 8.422 lb/g (round to 8.4)
# Barley Wine with a FG of 1.030: 8.345 x 1.030 = 8.595 lb/g (round to 8.6)
def lbsToOz(lbs):
    tare = lbs - 17;
    return (tare / 8.5) * 128;

def read_scales(ser):
    while 1 :
        line = ser.readline()
        if not line.strip():
            continue
        weights = line.split(';')

        for index, weight in enumerate(weights):
            oz = lbsToOz(maprange(float(weight), keg_data[index]['analogA'], keg_data[index]['analogB']))
            kegs[index] = int(oz)  # TODO: Some kinda rounding
        time.sleep(2)

# Render all the static content 'as is'
@app.route("/static/<path:path>")
def render_static(path):
    return send_from_directory('static', path)

# Main page of the app
@app.route("/")
def index():
    return render_template('index.html')

# Query for the current amount of liuqid in a keg by number
# Examples:
# HTTP GET /kegs  => 234.12;234.12
@app.route("/kegs")
def amount_in_kegs():
    return ";".join([str(x) for x in kegs.values()])

if __name__ == "__main__":

    #ser = serial.Serial('/dev/ttyACM0', 9600)

    # Fake class which is like serial
    class MockSerial:
        def readline(self):
            return "415.30;387.60"
    ser = MockSerial()

    # Start the weight sensor in the background
    thread = threading.Thread(target=read_scales, args=(ser,))
    thread.daemon = True
    thread.start()

    # Start the webserver
    app.run(debug=True)
