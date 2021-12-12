#!/snap/bin/pypy3

file = open("../data/day12.txt", "rt")
data = [x.split('-') for x in file.read().split('\n') if x != '']
file.close()

part2 = True
r = 0

connections = {}

for c1,c2 in data:
	if c1 not in connections:
		connections[c1] = []
	if c2 not in connections:
		connections[c2] = []
	connections[c1].append(c2)
	connections[c2].append(c1)

def search(prefix, nexts):
	global r
	for n in nexts:
		if n == 'start':
			continue
		if n == 'end':
			r += 1
			continue
		new_prefix = prefix.copy()
		if n.islower() and n in new_prefix:
			if part2:
				if new_prefix[0].isupper():
					continue
				else:
				 	new_prefix[0] = new_prefix[0].upper()
			else:
				continue
		new_prefix.append(n)
		search(new_prefix, connections[n])

search(['start'], connections['start'])

print(r)
