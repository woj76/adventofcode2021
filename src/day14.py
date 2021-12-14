#!/snap/bin/pypy3

file = open("../data/day14.txt", "rt")
[polymer, ps] = file.read().strip().split('\n\n')
file.close()

part2 = True

prods = {}

for p in ps.strip().split('\n'):
	[l,r] = p.split(' -> ')
	prods[l] = r

pairs = {}

for i in range(1, len(polymer)):
	p = polymer[i-1:i+1]
	if p not in pairs:
		pairs[p] = 0
	pairs[p] += 1

for _ in range(40 if part2 else 10):
	new_pairs = {}
	for p,c in pairs.items():
		n = prods[p]
		p1 = p[0] + n
		p2 = n + p[1]
		if p1 not in new_pairs:
			new_pairs[p1] = 0
		if p2 not in new_pairs:
			new_pairs[p2] = 0
		new_pairs[p1] += c
		new_pairs[p2] += c
	pairs = new_pairs

counts = { polymer[0] : 1 }

for p,c in pairs.items():
	t = p[1]
	if t not in counts:
		counts[t] = 0
	counts[t] += c

min_c, max_c = float('inf'), float('-inf')

for l,c in counts.items():
	min_c = min(c, min_c)
	max_c = max(c, max_c)

print(max_c - min_c)
