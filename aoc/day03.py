# aoc 2021
# day 3: binary diagnostic

def part1():

	file = open("day03.txt", "r")

	# read first line of bits
	ones = [int(i) for i in file.readline().strip()]
	rows = 1

	for line in file:
		rows += 1
		for i in range(len(ones)):
			ones[i] += int(line[i])

	# calculate gamma and epsilon rates
	zeroes = [rows - i for i in ones]
	gammas = [int(o > z) for (o, z) in zip(ones, zeroes)]
	epsilons = [int(o < z) for (o, z) in zip(ones, zeroes)]

	# convert list of a binary's bits to decimal
	gamma = int(int("".join(map(str, gammas)), base = 2))
	epsilon = int(int("".join(map(str, epsilons)), base = 2))

	print(gamma * epsilon)

def part2():
	# read numbers into a list
	file = open("day03.txt", "r")
	lines = file.readlines()

	def helper(lines, oxygen = True, column = 0):

		if len(lines) == 1:
			return int(int("".join(map(str, lines)), base = 2))

		positions_of_ones, positions_of_zeroes = [], []
		for r in range(len(lines)):
			# count all 1s and 0s
			if int(lines[r][column]) == 1:
				positions_of_ones.append(r)
			else:
				positions_of_zeroes.append(r)
		ones, zeroes = len(positions_of_ones), len(positions_of_zeroes)

		# find out most and least common values
		if oxygen:
			remaining_lines = [lines[i] for i in positions_of_ones] if int(ones >= zeroes) else [lines[i] for i in positions_of_zeroes]
		else:
			remaining_lines = [lines[i] for i in positions_of_ones] if int(ones < zeroes) else [lines[i] for i in positions_of_zeroes]
		
		return helper(remaining_lines, oxygen, column + 1)

	print(helper(lines, True) * helper(lines, False))	# o2 * co2

part1()
part2()