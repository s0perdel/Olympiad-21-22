#Task C

a = int(input())
b = int(input())
c = int(input())

res = 0

def findAvg(a1,a2):
	if a1 > a2:
		a = list(range(a2,a1+1))
	else:
		a = list(range(a1,a2+1))
	while len(a) > 2:
		a.pop(0)
		a.pop(-1)
	return a[0]
	
while True:	
	#print([a,b,c,res])
	if b-a > 1:
		c = findAvg(a,b)
		res += 1
		#print([a,b,c,res])
		if c-a > 1:
			b = findAvg(a,c)
			res += 1
			#print([a,b,c,res])
		elif b-c > 1:
			a = findAvg(c,b)
			res += 1
			#print([a,b,c,res])
		else:
			break
	elif c-b > 1:
		a = findAvg(b,c)
		res += 1
		#print([a,b,c,res])
		if c-a > 1:
			#print([a,b,c,res])
			b = findAvg(a,c)
			res += 1
		elif b-c > 1:
			c = findAvg(b,a)
			res += 1
			#print([a,b,c,res])
		else:
			break
	else:
		break
	
print(res)