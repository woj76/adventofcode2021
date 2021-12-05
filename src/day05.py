#!/snap/bin/pypy3

file = open("../data/day05.txt", "rt")
data = [tuple([int(y) for y in x.split(',')]) for x in file.read().replace(' -> ', ',').split('\n') if x != '']
file.close()

part2 = True
r = 0

size = 1001
plane = [[0]*size for x in range(size)]

for x1,y1,x2,y2 in data:
	dx = x2 - x1
	dy = y2 - y1
	if part2 or dx == 0 or dy == 0:
		s = max(abs(dx), abs(dy)) + 1
		dx = 1 if dx > 0 else (-1 if dx < 0 else 0)
		dy = 1 if dy > 0 else (-1 if dy < 0 else 0)
		i, j = x1, y1
		for k in range(s):
			plane[j][i] += 1
			i += dx
			j += dy

for i in range(size):
	for j in range(size):
		if plane[j][i] > 1:
			r += 1

print(r)
