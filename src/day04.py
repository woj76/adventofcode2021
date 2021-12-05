#!/snap/bin/pypy3

file = open("../data/day04.txt", "rt")
data = [x for x in file.read().strip().split('\n\n') if x != '']
file.close()

draws = [int(x.strip()) for x in data[0].split(',')]
boards = []

for d in data[1:]:
	b = [[int(y) for y in x.split(' ') if y != ''] for x in d.split('\n')]
	boards.append(b)

def draw(board, num):
	for i in range(0, 5):
		for j in range(0, 5):
			if board[j][i] == num:
				board[j][i] = -board[j][i]

def check_win(board):
	for i in range(0, 5):
		win = True
		for j in range(0, 5):
			if board[j][i] > 0:
				win = False
				break
		if win:
			break
	if win:
		return win
	for j in range(0, 5):
		win = True
		for i in range(0, 5):
			if board[j][i] > 0:
				win = False
				break
		if win:
			break
	return win

def collect(board):
	r = 0
	for i in range(0, 5):
		for j in range(0, 5):
			e = board[j][i]
			if e > 0:
				r += e
	return r

part2 = True

wins_until_report = len(boards) if part2 else 1
wins = [0] * len(boards)

for n in draws:
	for i,b in enumerate(boards):
		if wins[i] == 1:
			continue
		draw(b, n)
		if check_win(b):
			wins[i] = 1
			if sum(wins) == wins_until_report:
				print(n * collect(b))
				exit()
