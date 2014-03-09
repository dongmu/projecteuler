#!/usr/bin/python

n = int(raw_input("Please input the number: \n"))

i3 = n / 3
i5 = n / 5 - 1
i15 = n / 15
sumall = 0

while (i3 != 0):
	sumall += 3 * i3
	i3 -= 1

while (i5 != 0):
	sumall += 5 * i5
	i5 -= 1

while (i15 != 0):
	sumall -= 15 * i15
	i15 -= 1

print sumall
