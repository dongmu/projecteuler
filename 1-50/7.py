#!/usr/bin/python

import math

count = 2
n = 3
primelist = [2,3]

while True:
	if count == 10001:
		break

	n += 2
	for prime in primelist:
		if prime > (int)(math.sqrt(n)):
			count += 1
			primelist.append(n)
			break
		if n % prime == 0:
			break

#print primelist
print n
