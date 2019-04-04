def binary(value, length):
	result = bin(value)[2:]
	while len(result) < length:
		result = "0" + result
	return result

def binary_list(value):
	result = []
	for c in reverse(value):
		result.append(c)
	return result

def reverse(value):
	return value[::-1]

def get_bin(value, length):
	return binary_list(binary(value, length))
