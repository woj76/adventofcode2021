#!/snap/bin/pypy3

file = open("../data/day25.txt", "rt")
data = [list(x) for x in file.read().split('\n') if x != '']
file.close()

r = 0

x_size = len(data[0])
y_size = len(data)

while True:
	to_move_east = {}
	for x in range(x_size):
		for y in range(y_size):
			if data[y][x] != '>':
				continue
			x1 = (x+1) % x_size
			if data[y][x1] == '.':
				to_move_east[(x,y)] = (x1,y)
	for (fx,fy),(tx,ty) in to_move_east.items():
		data[ty][tx] = '>'
		data[fy][fx] = '.'
	to_move_south = {}
	for x in range(x_size):
		for y in range(y_size):
			if data[y][x] != 'v':
				continue
			y1 = (y+1) % y_size
			if data[y1][x] == '.':
				to_move_south[(x,y)] = (x,y1)
	for (fx,fy),(tx,ty) in to_move_south.items():
		data[ty][tx] = 'v'
		data[fy][fx] = '.'
	r += 1
	if not to_move_east and not to_move_south:
		break

print(r)
