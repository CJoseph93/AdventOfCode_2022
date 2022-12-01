import os

def main():
	file1 = open('input.txt', 'r')
	lines = file1.readlines()
	results = [0]
	for line in lines:
		if line == '\n':
			results.append(0)
		else:
			results[len(results) - 1] += int(line)
	
	results.sort(reverse=True)
	print(results[0]) # First problem
	print(results[0] + results[1] + results[2]) #second problem
	
if __name__ == "__main__":
    main()