# aoc 2021
# day 2: dive

inp = open("day02.txt", "r").readlines()
inp = [i.split(" ") for i in inp]

def part1():
	horizon, depth = 0, 0

	for dir, x in inp:
		x = int(x)

		if dir == "forward":
			horizon += x
		elif dir == "down":
			depth += x
		else: # up
			depth -= x

	print(horizon * depth)

def part2():
	horizon, depth, aim = 0, 0, 0

	for dir, x in inp:
		x = int(x)

		if dir == "down":
			aim += x
		elif dir == "up":
			aim -= x
		else: # forward
			horizon += x
			depth += aim * x

	print(horizon * depth)

part1()
part2()