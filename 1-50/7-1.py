#!/usr/bin/python

import math

count = 2
n = 3
primelist = [2,3]

while True:
	if count == 10001:
		break

	n += 2
	booln = True
	tmp = (int)(math.sqrt(n))+1
	for prime in primelist:
		if prime > tmp:
			break
		if n % prime == 0:
			booln = False
			break
	
	if booln:
		count += 1
		primelist.append(n)

#print primelist
print n
