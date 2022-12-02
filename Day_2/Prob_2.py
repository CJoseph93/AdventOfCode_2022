import os

def findWinner(a, b):
	if b == 1:
		if a == 1:
			return 3
		elif a == 2:
			return 1
		else:
			return 2
	elif b == 2:
		return a + 3
	else:
		if a == 1:
			return 8
		elif a == 2:
			return 9
		else:
			return 7

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