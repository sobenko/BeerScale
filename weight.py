#!python2.6
import serial
import time

loadA = 0.0
loadB = 55.0
analogvalA_keg1 = 22.91
analogvalB_keg1 = 415.30
analogvalA_keg2 = 11
analogvalB_keg2 = 387.60


def maprange(s,analogvalA,analogvalB):
	return loadA + ((s - analogvalA) * (loadB - loadA) / (analogvalB - analogvalA))
	#return  analogvalA + ((s - loadA) * (analogvalB - analogvalA) / (loadB - loadA))

# 128 oz in a gallon
# http://www.brewangels.com/Beerformation/Weight.html
# Light Lager with a FG of 1.008: 8.345 x 1.008 = 8.422 lb/g (round to 8.4)
# Barley Wine with a FG of 1.030: 8.345 x 1.030 = 8.595 lb/g (round to 8.6)
def lbsToOz(lbs):
		tare = lbs - 17;
		return (tare / 8.5) * 128;

ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
	line = ser.readline()
	if not line.strip():
		continue
	#print line
	weights = line.split(';')
	with open('keg1.txt', 'w') as f:
		f.write(str(lbsToOz(maprange(float(weights[0]),analogvalA_keg1, analogvalB_keg1)))
		f.write(";")
		f.write(str(lbsToOz(maprange(float(weights[1]),analogvalA_keg2, analogvalB_keg2)))
	
