#Task A
import math

a = 0
b = []
l = []
r = []

while a <  4:
	b = input().split(" ")
	l.append(b[0])
	r.append(b[1])
	a += 1

del a
del b

i = 0
tries = 1
seconds = 0

while i < 4:
	tries = tries * (int(r[i]) - int(l[i]) + 1)
	i += 1
	
if tries < 5:
	seconds = tries * 30
else:
	seconds = (tries * 30) + math.floor(tries/5)*300
	
print(tries)
print(seconds)