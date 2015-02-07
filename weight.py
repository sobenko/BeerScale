#!python2.6
import serial
import time

loadA = 0.0
loadB = 55.0
analogvalA-keg1 = 22.91
analogvalB-keg1 = 415.30
analogvalA-keg2 = 11
analogvalB-keg2 = 387.60

def maprange(s,analogvalA,analogvalB):
	return loadA + ((s - analogvalA) * (loadB - loadA) / (analogvalB - analogvalA))
	#return  analogvalA + ((s - loadA) * (analogvalB - analogvalA) / (loadB - loadA))

ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
	line = ser.readline()
	if not line.strip():
		continue
	print line
	weights = line.split(':')
	with open('keg1.txt', 'w') as f:
		f.write(str(maprange(float(weights[0], analogvalA-keg1, analogvalB-keg1))))
	
	with open('keg2.txt', 'w') as f:
		f.write(str(maprange(float(weights[1], analogvalA-keg2, analogvalB-keg2))))
	
