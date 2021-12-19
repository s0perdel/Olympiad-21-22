#Task B

secret = list(input())
password = []

i = 0
hunt = 0

while i < 4:
	j = 1
	while True:
		hunt = list(str(j**3))
		if hunt[-1] == secret[i]:
			password.append(j)
			break
		j += 1
	i += 1
	
password = int(password[0])*1000+int(password[1])*100+int(password[2])*10+int(password[3])*1
print(password)