# aoc 2021
# day 3: binary diagnostic

file = open("day03.txt", "r")

def part1():

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
	lines = file.readlines()
	ncols = len(lines[0])

	def helper(column, lines, common=True):
		nrows = len(lines)

		if nrows == 1:
			print(lines)
			return int(int("".join(map(str, lines)), base = 2))

		positions_of_ones = []
		positions_of_zeroes = []
		ones, zeroes = 0, 0
		for r in range(nrows):
			line = lines[r]
			# count all 1s and 0s
			if int(line[column]) == 1:
				ones += 1
				positions_of_ones.append(r)
			else:
				positions_of_zeroes.append(r)
		zeroes = nrows - ones

		# find out most and least common values
		if common:
			desired = int(ones > zeroes)
			if desired == 1:
				remaining_lines = [lines[i] for i in positions_of_ones]
			else:
				remaining_lines = [lines[i] for i in positions_of_zeroes]
		else:
			desired = int(ones < zeroes)
			if desired == 1:
				remaining_lines = [lines[i] for i in positions_of_ones]
			else:
				remaining_lines = [lines[i] for i in positions_of_zeroes]
		print(remaining_lines)
		print()
		return helper(column + 1, remaining_lines, common)

	o2 = helper(0, lines, True)
	print(o2)
	#co2 = helper(0, lines, False)
	#print(o2, co2, str(o2 * co2))

part2()