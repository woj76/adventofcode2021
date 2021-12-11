#!/snap/bin/pypy3

file = open("../data/day11.txt", "rt")
data = [[int(y) for y in x] for x in file.read().split('\n') if x != '']
file.close()

part2 = True
r = 0

y_size = len(data)
x_size = len(data[0])

def n(x, y):
	r = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
	r = [(x,y) for x,y in r if x != -1 and x != x_size and y != -1 and y != y_size]
	return r

c = 0
while True:
	flashed = set()
	to_check = []
	for j in range(y_size):
		for i in range(x_size):
			to_check.append((i,j))
	first_round = True
	while to_check:
		new_to_check = []
		for i,j in to_check:
			e = data[j][i]
			if e == 0 and not first_round:
				continue
			e = (e + 1) % 10
			if e == 0:
				flashed |= {(i,j)}
				new_to_check += n(i,j)
			data[j][i] = e
		to_check = new_to_check
		first_round = False
	c += 1
	if not part2:
		r += len(flashed)
		if c == 100:
			break
	else:
		if len(flashed) == x_size * y_size:
			r = c
			break

print(r)
