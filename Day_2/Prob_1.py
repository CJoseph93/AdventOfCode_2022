import os

def findWinner(a, b):
	if a == b:
		return 3 + b
	elif b == 1 and a == 3:
		return b + 6
	elif b == 2 and a == 1:
		return b + 6
	elif b == 3 and a == 2:
		return b + 6
	else:
		return b

def main():
	file1 = open('input.txt', 'r')
	lines = file1.readlines()
	result = 0
	for line in lines:
		test = line.split()
		a = 1
		b = 1
		if test[0] == 'B':
			a = 2
		elif test[0] == 'C':
			a = 3
		if test[1] == 'Y':
			b = 2
		elif test[1] == 'Z':
			b = 3
		result += findWinner(a, b)
	
	print(result)

	
if __name__ == "__main__":
    main()