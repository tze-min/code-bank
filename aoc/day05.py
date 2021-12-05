# aoc 2021
# day 5: hydrothermal venture

def input_generator(path):
	with open(path, "r") as f:
		for line in f:
			p1, p2 = line.strip().split(" -> ")
			x1, y1 = map(int, p1.split(","))
			x2, y2 = map(int, p2.split(","))
			yield x1, y1, x2, y2

def part1():
	sparse_matrix = {}

	for x1, y1, x2, y2 in input_generator("day05.txt"):
		if x1 != x2 and y1 != y2:
			continue

		step_x = 0 if x1 == x2 else (1 if x1 < x2 else -1)
		step_y = 0 if y1 == y2 else (1 if y1 < y2 else -1)
		distance = abs(x1 - x2) if y1 == y2 else abs(y1 - y2)

		for i in range(distance + 1):
			key = (step_x * i + x1, step_y * i + y1)
			sparse_matrix[key] = sparse_matrix[key] + 1 if key in sparse_matrix else 1

	print(len(list(filter(lambda x: x >= 2, sparse_matrix.values()))))

def part2():
	sparse_matrix = {}

	for x1, y1, x2, y2 in input_generator("day05.txt"):
		step_x = 0 if x1 == x2 else (1 if x1 < x2 else -1)
		step_y = 0 if y1 == y2 else (1 if y1 < y2 else -1)
		distance = abs(x1 - x2) if x1 != x2 else abs(y1 - y2)

		for i in range(distance + 1):
			key = (step_x * i + x1, step_y * i + y1)
			sparse_matrix[key] = sparse_matrix[key] + 1 if key in sparse_matrix else 1

	print(len(list(filter(lambda x: x >= 2, sparse_matrix.values()))))

part1()
part2()