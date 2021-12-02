# aoc 2021
# day 1: sonar sweep

inp = open("day01.txt", "r").readlines()
inp = [int(i) for i in inp]

def part1():
	c = 0
	for i in range(len(inp[:len(inp)-1])):
		if inp[i] < inp[i+1]:
			c += 1
	print(c)

def part2():
	c = 0
	for i in range(len(inp[:len(inp)-3])):
		if inp[i] < inp[i+3]:
			c += 1
	print(c)

part1()
part2()