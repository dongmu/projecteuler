#!/usr/bin/python

import math

input_n = int(raw_input("Please input the number:\n"))


def isPrime(n):
	tmp = math.sqrt(n)
	for i in range(2, int(tmp)+1):
		if n % i == 0:
			return False
	
	return True

def getBigPri(n):
	tmp = int(math.sqrt(n)) + 1
	tmp2 = n % tmp
	while (tmp2 != 0):
		tmp -= 1
		tmp2 = n % tmp

	tmp2 = n / tmp

	if (isPrime(tmp) & isPrime(tmp2)):
		if (tmp > tmp2):
			return tmp
		else:
			return tmp2
	elif (isPrime(tmp)):
		i = getBigPri(tmp2)
		if (tmp > i):
			return tmp
		else:
			return i
	elif (isPrime(tmp2)):
		i = getBigPri(tmp)
		if (i > tmp2):
			return i
		else:
			return tmp2
	else:
		i1 = getBigPri(tmp)
		i2 = getBigPri(tmp2)
		if (i1 > i2):
			return i1
		else:
			return i2

print getBigPri(input_n)
