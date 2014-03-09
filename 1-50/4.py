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
l2 = range(100, 999)
l1.reverse()
l2.reverse()

s = []

for i in l1:
	for j in l2:
		if (isPalin(i*j)):
			s.append([i,j])
	
l3 = []
tmp = []
for i in s:
	print i
	if l3 == []:
		tmp = i[:]
		tmp.append(tmp[0]*tmp[1])
		l3=tmp[:]
		continue
	
	if l3[0] >= i[0] and l3[1] >= i[1]:
		continue
	elif l3[0]*l3[1] >= i[0]*i[1]:
		continue
	else:
		i.append(i[0]*i[1])
		l3=i[:]

print l3




#print isPalin(1001)
#print isPalin(3232)
