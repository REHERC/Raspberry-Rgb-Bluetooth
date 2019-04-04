import time
import RPi.GPIO as GPIO

def led_init():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)

def led_set(r_out, g_out, b_out):
	print(r_out)
	print(g_out)
	print(b_out)
	GPIO.output(11, int(r_out))
	GPIO.output(12, int(g_out))
	GPIO.output(13, int(b_out))
