#!/usr/bin/python
# Python has a recursion deepth which limits my function
import sys
sys.setrecursionlimit(100000)

def gcd(i, j):
	try:
		if i == j:
			return i
		elif i > j:
			return gcd(i-j, j)
		else:
			return gcd(i, j-i)
	finally:
		s=1

sum1 = 2

for i in range(11, 21):
	print i
	print sum1
	sum1 = sum1 * i / gcd(i, sum1)

print sum1
