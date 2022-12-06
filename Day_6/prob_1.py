import os

def main():
	file1 = open('input.txt', 'r')
	lines = file1.readlines()
	myStr = lines[0]
	result = 0
	for x in range(3, len(myStr)):
		y = myStr[x - 3] + myStr[x - 2] + myStr[x - 1] + myStr[x]
		if len(set(y)) == len(y):
			result = x + 1
			break
	print(result)

if __name__ == "__main__":
    main()