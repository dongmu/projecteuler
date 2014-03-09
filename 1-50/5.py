#!/usr/bin/python
# Python has a recursion deepth which limit my function
import sys
sys.setrecursionlimit(100000)

def gcd(i, j):
	try:
		if i == j:
			return i
		elif i > j:
			if i%j == 0:
				return j
			else:
				return gcd(i%j, j)
		else:
			if j%i == 0:
				return i
			else:
				return gcd(i, j%i)
	finally:
		s=1

sum1 = 2

for i in range(1,21):
#	print i
#	print sum1
	sum1 = sum1 * i / gcd(i, sum1)

print sum1
