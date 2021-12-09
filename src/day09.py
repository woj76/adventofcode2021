#!/snap/bin/pypy3

file = open("../data/day09.txt", "rt")
data = [[int(y) for y in x] for x in file.read().split('\n') if x != '']
file.close()

part2 = True

y_size = len(data)
x_size = len(data[0])

def n(x, y):
	r = [(x-1,y), (x+1,y), (x,y-1), (x, y+1)]
	r = [(x,y) for x,y in r if x != -1 and x != x_size and y != -1 and y != y_size]
	return r


basins = []

for j in range(y_size):
	for i in range(x_size):
		s = True
		for nx,ny in n(i,j):
			if data[j][i] >= data[ny][nx]:
				s = False
				break
		if s:
			basins.append((i,j))

if not part2:
	r = 0
	for i,j in basins:
		r += data[j][i] + 1
else:
	basin_sizes = []
	for i,j in basins:
		pp = {(i,j)}
		to_visit = {(x, y) for x,y in n(i,j) if data[y][x] < 9}
		while len(to_visit) > 0:
			pp |= to_visit
			to_visit = set()
			for (ii,jj) in pp:
				to_visit |= {(x, y) for x,y in n(ii,jj) if data[y][x] < 9 and (x,y) not in pp}
		basin_sizes.append(len(pp))
	basin_sizes.sort()
	l = len(basin_sizes)
	r = basin_sizes[l-1] * basin_sizes[l-2] * basin_sizes[l-3]

print(r)
