#!/usr/bin/python

def isPalin(n):
	a = []
	tmp = n
	while(True):
		if (tmp == 0):
			break

		i = tmp % 10
		tmp = tmp / 10

		a.append(i)
	
	b = a[:]
	b.reverse()

	if a == b:
		return True
	else:
		return False


l1 = range(100, 999)
l1.reverse()

s = []

for i in l1:
	l2 = range(100,i)
	l2.reverse()
	for j in l2:
		if (isPalin(i*j)):
			if s == []:
				s.append(i)
				s.append(j)
			elif s[0] == i and s[1] > j:
				continue
			elif s[1] == j and s[0] > i:
				continue
			elif s[0]*s[1] >= i*j:
				continue
			else:
				s[0] = i
				s[1] = j

print s
