from sys import argv

lesserNum = int(argv[1])

for num in argv[1:]:
	num = int(num)
	if lesserNum > num :
		lesserNum = num

print(lesserNum)