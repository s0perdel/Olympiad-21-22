#Task D

mCount = input()
mAll = list(input().split(" "))
oCount = input()
oAll = list(input().split(" "))

Om = []
Mo = []
res1 = ""
res2 = ""

for o in oAll:
	if not o in mAll:
		Om.append(o)

for m in mAll:
	if not m in oAll:
		Mo.append(m)

i = 0
while i < len(Om):
	res1 += Om[i]
	res1 += " "
	i += 1
	
i = 0
while i < len(Mo):
	res2 += Mo[i]
	res2 += " "
	i += 1
	
print(res1)
print(res2)