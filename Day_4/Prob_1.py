import os

def checkPair(elf1, elf2):
	if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
		return 1
	elif int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
		return 1
	return 0

def main():
	file1 = open('input.txt', 'r')
	lines = file1.readlines()
	result = 0
	for line in lines:
		a, b = line.split(',')
		elf1 = a.split('-')
		elf2 = b.split('-')
		result += checkPair(elf1, elf2)
	print(result)
	
if __name__ == "__main__":
    main()