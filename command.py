from led import *
from binary import *

def decompose(command):
	flag = 0
	item = ""
	tokens = []
	command_postfix = command + " "
	for index, char in enumerate(command_postfix):
		if (char == ' ') & (flag == 0):
			tokens.append(item)
			item = ""
		elif char == '"':
			flag = 1 - flag
		else:
			item += char
	return tokens

def run(command):
	parse(decompose(command))

def get(tokens, index):
	if len(tokens) >= index + 1:
		return tokens[index]
	else:
		return "error"

def getl(tokens, index):
	return get(tokens, index).lower()

def parse(tokens):
	if getl(tokens, 0) == "color":
		bits = get_bin(int(getl(tokens, 1)), 3)
		led_set(bits[2], bits[1], bits[0])
	elif getl(tokens, 0) == "print":
		print(get(tokens, 1))
