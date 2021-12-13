#!/snap/bin/pypy3

file = open("../data/day13.txt", "rt")
[coords,folds] = file.read().split('\n\n')
file.close()

part2 = True

x_min = y_min = float('inf')
x_max = y_max = float('-inf')

dots = {}

def print_dots():
	for y in range(y_max):
		for x in range(x_max):
			if (x,y) in dots:
				print('#', end='')
			else:
				print('.', end='')
		print()

def fold_x(xf):
	global x_max
	for x,y in dots.copy():
		if x > xf:
			dots[(2*xf - x,y)] = True
			del dots[(x,y)]
	x_max = xf

def fold_y(yf):
	global y_max
	for x,y in dots.copy():
		if y > yf:
			dots[(x,2*yf - y)] = True
			del dots[(x,y)]
	y_max = yf

for line in coords.split('\n'):
	[x, y] = line.split(',')
	x,y = int(x), int(y)
	dots[(x,y)] = True
	x_min = min(x, x_min)
	y_min = min(y, y_min)
	x_max = max(x, x_max)
	y_max = max(y, y_max)
x_max += 1
y_max += 1

for d in folds.strip().split('\n'):
	dir = d[11:12]
	v = int(d[13:])
	if dir == 'x':
		fold_x(v)
	elif dir == 'y':
		fold_y(v)
	if not part2:
		break

if part2:
	print_dots()
else:
	print(len(dots))
