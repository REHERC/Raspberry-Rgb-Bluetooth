import serial
import time
from command import *
from led import *

led_init()

ser = serial.Serial("/dev/serial0", 9600)

compteur = 0
while 1:
	if ser.inWaiting() > 0:
		command = ""
		while ser.inWaiting() > 0:
			command = command + str(ser.read())
		run(command)
