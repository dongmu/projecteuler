#!/usr/bin/python

top = int(raw_input("Please input the number:\n"))

n = 0
n1 = 2
n2 = 3
n3 = 5

while (n3 < top):
	n += n1
	n1 = n2 + n3
	n2 = n1 + n3
	n3 = n1 + n2

print n
