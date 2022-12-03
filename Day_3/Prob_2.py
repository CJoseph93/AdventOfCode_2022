import os

def calcPriority(a, b, c):
	result = 0
	for x in a:
		for y in b:
			for z in c:
				if x == y == z:
					if x.isupper():
						result += 26
					result += ord(x.lower()) - 96
					return result

def main():
	file1 = open('input.txt', 'r')
	lines = file1.readlines()
	result = 0
	for x in range(0, len(lines)):
		if x % 3 == 0:
			a = lines[x]
			b = lines[x + 1]
			c = lines[x + 2]
			result += calcPriority(a, b, c)
		
	print(result)

	
if __name__ == "__main__":
    main()