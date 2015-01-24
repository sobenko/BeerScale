#!python2.6
import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
	line = ser.readline()
	if not line.strip():
		continue
	f = open('keg1.txt','w')
	f.write(line)
	f.close()
