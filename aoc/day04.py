# aoc 2021
# day 4: giant squid

def part1():
	file = open("day04.txt", "r")
	input = [int(i) for i in file.readline().split(",")]
	raw = file.readlines()[1:] + ["\n"]

	# represent boards
	all_boards, board = [], []
	for row in raw:
		if row == "\n":
			all_boards.append(board)
			board = []
			continue
		board.append([int(i) for i in row.split()])

	# represent bingos
	nboards = len(all_boards)
	bingo_rows = [[0]*5 for i in range(nboards)]
	bingo_cols = [[0]*5 for i in range(nboards)]
	sums_of_called = [0 for i in range(nboards)]

	# begin bingo
	def find_bingo():
		for i in input:
			for b in range(nboards):
				for r in range(5):
					for c in range(5):
						
						if all_boards[b][r][c] == i:
							bingo_rows[b][r] += 1
							bingo_cols[b][c] += 1
							sums_of_called[b] += i

							if bingo_rows[b][r] == 5 or bingo_cols[b][c] == 5:
								print("board", b, "won!")
								board_sum = sum(sum(x) for x in all_boards[b])
								return i * (board_sum - sums_of_called[b])

	res = find_bingo()
	print(res)


def part2():
	file = open("day04.txt", "r")
	input = [int(i) for i in file.readline().split(",")]
	raw = file.readlines()[1:] + ["\n"]

	# represent boards
	all_boards, board = [], []
	for row in raw:
		if row == "\n":
			all_boards.append(board)
			board = []
			continue
		board.append([int(i) for i in row.split()])

	# represent bingos
	nboards = len(all_boards)
	bingo_rows = [[0 for j in range(5)] for i in range(nboards)]
	bingo_cols = [[0 for j in range(5)] for i in range(nboards)]
	sums_of_called = [0 for i in range(nboards)]

	# begin bingo
	won_boards = []

	for i in input:
		for b in range(nboards):
			if b in won_boards:
				continue

			def find_bingo(b):
				for r in range(5):
					for c in range(5):

						if all_boards[b][r][c] == i:
							bingo_rows[b][r] += 1
							bingo_cols[b][c] += 1
							sums_of_called[b] += i

							if bingo_rows[b][r] == 5 or bingo_cols[b][c] == 5:
								won_boards.append(b)

								if len(won_boards) == nboards:
									print("board", b, "is the last to win!")
									board_sum = sum(sum(x) for x in all_boards[b])
									print(i * (board_sum - sums_of_called[b]))
									return
								return

			find_bingo(b)

part1()
part2()