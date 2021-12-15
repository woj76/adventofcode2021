#!/snap/bin/pypy3

import heapq
from collections import defaultdict

file = open("../data/day15.txt", "rt")
data = [[int(y) for y in x] for x in file.read().split('\n') if x != '']
file.close()

part2 = True

def up_list(l):
	r = []
	for e in l:
		e += 1
		if e == 10:
			e = 1
		r.append(e)
	return r

y_size = len(data)
x_size = len(data[0])

def n(x, y):
	r = [(x-1,y), (x+1,y), (x,y-1), (x, y+1)]
	r = [(x,y) for x,y in r if x != -1 and x != x_size and y != -1 and y != y_size]
	return r

if part2:
	for d in data:
		dd = d.copy()
		for _ in range(4):
			ul = up_list(dd)
			for x in ul:
				d.append(x)
			dd = ul
	for i in range(4):
		for y in range(y_size):
			data.append(up_list(data[y+i*y_size]))

y_size = len(data)
x_size = len(data[0])

visited = set()
q = []
dist = defaultdict(lambda : float('inf'))
dist[(0,0)] = 0

heapq.heappush(q, (0, (0,0)))

while q:
	_, u = heapq.heappop(q)
	visited.add(u)
	if u == (x_size-1,y_size-1):
		break
	for v in [y for y in n(u[0],u[1]) if y not in visited]:
		alt = dist[u] + data[v[1]][v[0]]
		if alt < dist[v]:
			dist[v] = alt
			heapq.heappush(q, (alt, v))

print(dist[(x_size-1,y_size-1)])
