#!/snap/bin/pypy3

file = open("../data/day20.txt", "rt")
data = [x for x in file.read().strip().split('\n\n') if x != '']
file.close()

part2 = True

alg = data[0]

plane = {}
x_min = y_min = x_max = y_max = 0

for d in data[1].split('\n'):
	x_max = 0
	for c in d:
		if c == '#':
			plane[(x_max,y_max)] = True
		x_max += 1
	y_max += 1

def get_xy(p, x, y):
	if x < x_min or x >= x_max or y < y_min or y >= y_max:
		return last_outer
	return (x,y) in p

def collect_bits(p, x, y):
	lst = [(x-1,y-1), (x,y-1), (x+1,y-1),
	     (x-1,y),   (x,y),   (x+1,y),
		 (x-1,y+1), (x,y+1), (x+1,y+1)]
	s = ""
	for i,j in lst:
		s += ("1" if get_xy(p,i,j) else "0")
	return int(s,2)

last_outer = False

for _ in range(50 if part2 else 2):
	new_plane = {}
	for x in range(x_min-2,x_max+2):
		for y in range(y_min-2,y_max+2):
			idx = collect_bits(plane,x,y)
			if alg[idx] == '#':
				new_plane[(x,y)] = True
	last_outer = not last_outer
	x_min -= 1
	y_min -= 1
	x_max += 1
	y_max += 1
	plane = new_plane

print(len(new_plane))
