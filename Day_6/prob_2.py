import os

def main():
	file1 = open('input.txt', 'r')
	lines = file1.readlines()
	myStr = lines[0]
	result = 0
	for x in range(13, len(myStr)):
		y = ""
		for z in range(x - 13, x + 1):
			y += myStr[z]
		if len(set(y)) == len(y):
			result = x + 1
			break
	print(result)

if __name__ == "__main__":
    main()