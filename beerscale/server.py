#!/usr/bin/env python

from flask import Flask
from flask import render_template, send_from_directory
import click

import threading
import serial
import time

from keg import Keg
from scale import Scale

app = Flask(__name__)


# TODO: We could read these from a config file or database instead of having
# them hardcoded.
keg1 = Keg(final_gravity=1.010, empty_weight=17)
keg2 = Keg(final_gravity=1.018, empty_weight=17)
kegs = [keg1, keg2]

# TODO: These can probably be in a config file since they aren't all that dynamic
# after initial installation
scale1 = Scale(low_read=22.91, low_weight=0.0, high_read=415.30, high_weight=55.0)
scale2 = Scale(low_read=11, low_weight=0.0, high_read=387.60, high_weight=55.0)
scales = [scale1, scale2]


def read_scales(ser):
    while True:
        line = ser.readline()
        if not line.strip():
            continue
        reads = line.split(';')

        for index, read in enumerate(reads):
            weight = scales[index].weight(analog_read=float(read))
            kegs[index].set_weight(weight)
        time.sleep(2)

# Render all the static content 'as is'
@app.route("/static/<path:path>")
def render_static(path):
    return send_from_directory('static', path)

# Main page of the app
@app.route("/")
def index():
    return render_template('index.html')

# Query for the current amount of liquid in a keg by number
# Examples:
# HTTP GET /kegs  => 234.12;234.12
@app.route("/kegs")
def amount_in_kegs():
    # TODO: Probably should render a json object for when the payload has more interesting data
    return ";".join([str(k.ounces) for k in kegs])

@click.command()
@click.option('--port', default=5000, help="Webserver port to use")
@click.option('--serial-port', default='/dev/ttyACM0', help="Serial port to read scale data from")
@click.option('--baud', default=9600, help="Baud rate to use for serial port")
@click.option('--debug', is_flag=True, help="Run in debug mode (with a fake serial interface)")
def run(port, serial_port, baud, debug):
    if debug:
        class MockSerial:
            def readline(self):
                return "415.30;387.60"
        ser = MockSerial()
    else:
        ser = serial.Serial(serial_port, int(baud))

    # Start the weight sensor in the background
    thread = threading.Thread(target=read_scales, args=(ser,))
    thread.daemon = True
    thread.start()

    # Start the webserver
    app.run(debug=debug, port=port)

if __name__ == "__main__":
    run()
