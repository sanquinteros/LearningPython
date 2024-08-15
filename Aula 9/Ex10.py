from sys import argv

num1 = int(argv[1])
num2 = int(argv[2])

if num1 > num2:
	print(f"{num1} \n {num2}")
elif num2 > num1:
	print(f"{num2} \n {num1}")
else:
	print(f"Ambos numeros são iguais")