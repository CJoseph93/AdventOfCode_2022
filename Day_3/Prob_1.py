import os

def calcPriority(a, b):
	result = 0
	for x in a:
		for y in b:
			if x == y:
				if x.isupper():
					result += 26
				result += ord(x.lower()) - 96
				return result

def main():
	file1 = open('input.txt', 'r')
	lines = file1.readlines()
	result = 0
	for line in lines:
		line1 = line[:len(line)//2]
		line2 = line[len(line)//2:]
		result += calcPriority(line1, line2)
		
	print(result)

	
if __name__ == "__main__":
    main()