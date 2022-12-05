import os
import re

def makeMove(move, grid):
	a = 0
	b = 0
	c = 0
	a,b,c = re.findall(r'\d+', move)
	a,b,c = int(a), int(b), int(c)
	for x in range(0, int(a)):
		grid[c - 1].insert(0, grid[b - 1][0])
		grid[b-1].pop(0)
	return grid

def main():
	file1 = open('input.txt', 'r')
	lines = file1.readlines()
	grid = [[], [], [], [], [], [], [], [], []]
	for line in lines:
		iter = 0
		for x in range(0, len(line)):
			if x % 4 == 0:
				if line[x] == "[":
					newCrate = line[x] + line[x+1] + line[x+2]
					grid[iter].append(newCrate)
				iter += 1
		if line[1] == "1":
			break
	for line in lines:
		if line[0] == "m":
			grid = makeMove(line, grid)
	
	for x in grid:
		print(x[0])

if __name__ == "__main__":
    main()