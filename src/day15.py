#!/snap/bin/pypy3

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

# This would be substantially quicker with proper binary search tree

def binary_search(arr, low, high, key):
	if high < low:
		return -1
	mid = (low + high) // 2
	if arr[mid] == key:
		return mid
	if key > arr[mid]:
		return binary_search(arr, mid+1, high, key)
	return binary_search(arr, low, mid-1, key)

q = {}
dist = {}
sl = []

for x in range(x_size):
	for y in range(y_size):
		d = 0 if x == 0 and y == 0 else float('inf')
		dist[(x,y)] = d
		sl.append((d,(x,y)))
		q[(x,y)] = True

while sl:
	u = sl[0][1]
	del sl[0]
	del q[u]
	if u == (x_size-1,y_size-1):
		break
	for v in [y for y in n(u[0],u[1]) if y in q]:
		vx, vy = v
		alt = dist[u] + data[vy][vx]
		if alt < dist[v]:
			idx = binary_search(sl, 0, len(sl), (dist[v],v))
			del sl[idx]
			found = False
			for i in range(0, idx):
				if alt < sl[i][0]:
					found = True
					break
			if not found:
				i = idx
			sl.insert(i, (alt,v))
			dist[v] = alt

print(dist[(x_size-1,y_size-1)])
