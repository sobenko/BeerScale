#!python2.6
import serial
import time

loadA = 0
analogvalA = 22.91
loadB = 55
analogvalB = 415.30

def maprange(s):
	return  analogvalA + ((s - loadA) * (analogvalB - analogvalA) / (loadB - loadA))

ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
	line = ser.readline()
	if not line.strip():
		continue
	f = open('keg1.txt','w')
	f.write(maprange(line))
	f.close()
