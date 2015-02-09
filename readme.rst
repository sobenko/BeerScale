##########
Beer Scale
##########

************
Introduction
************

This is a project for our homemade keggerator where we have several kegs on tap
but no way to determine how full each keg is. A series of postal scales were rigged
up with an Arduino to poll the weights of each keg. Using the empty and full weights
we are able to estimate how much beer is left in each keg.

This is a python webserver which polls the weight sensor data from the serial port
of the arduino and then displays the information about each tap on a webpage.

***************
Developer Setup
***************

Create a virtualenv for the project and install the dependencies::

  $ virtualenv -p python2.7 beerscale
  $ source beerscale/bin/activate
  $ pip install -r requirements.txt

Now run the webserver in debug mode::

  python beerscale/server.py --debug

Visit the website at: http://127.0.0.1:5000/

Running the server in debug mode will NOT connect to the serial port, instead
a mock serial port is used to pass fake test data to the webserver so that non-arduino
testing can be accomplished.

Server Options
--------------

--debug: enable debug mode

--port: the webserver port to use (default: 5000)

--serial-port: the serial port to listen on (default: /dev/ttyACM0)

--baud: the baud rate to use on the serial port (default: 9600)

Unit Testing
------------

TODO

********************
Scale Setup + Wiring
********************

TODO

*******************
Software Deployment
*******************

Building the server software is as easy as::

  $ python setup.py sdist

Installing the software (into a virtualenv)::

  $ pip install -U BeerScale-<version>.tar.gz

Running the server::

  $ beerscale --debug --port 8000
