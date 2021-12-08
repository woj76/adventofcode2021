#!/snap/bin/pypy3

file = open("../data/day08.txt", "rt")
data = [tuple(x.split(' | ')) for x in file.read().split('\n') if x != '']
file.close()

part2 = True

pats = []
outs = []

for p,o in data:
	pats.append([set(x) for x in p.split(' ')])
	outs.append([list(x) for x in o.split(' ')])

for p in pats:
	p.sort(key=len)

def get_mapping(ps):
	r = {}
	one = ps[0]
	seven = ps[1]
	four = ps[2]
	eight = ps[9]
	a = seven - one
	r[list(a)[0]] = 'a'
	comm_zero_six_nine = ps[6] & ps[7] & ps[8]
	cde = eight - comm_zero_six_nine
	c = cde & one
	r[list(c)[0]] = 'c'
	f = one - c
	r[list(f)[0]] = 'f'
	de = cde - c
	bd = four - one
	d = bd & de
	r[list(d)[0]] = 'd'
	b = bd - d
	r[list(b)[0]] = 'b'
	e = de - d
	r[list(e)[0]] = 'e'
	g = eight - a - b - c - d - e - f
	r[list(g)[0]] = 'g'
	return r

digits = {'abcefg':'0', 'cf':'1', 'acdeg':'2', 'acdfg':'3', 'bcdf':'4',
	'abdfg':'5', 'abdefg':'6', 'acf':'7', 'abcdefg':'8', 'abcdfg':'9'}

r = 0

for i,p in enumerate(pats):
	m = get_mapping(p)
	n = ""
	for o in outs[i]:
		ds = [m[x] for x in o]
		ds.sort()
		n += digits["".join(ds)]
	if part2:
		r += int(n)
	else:
		r += len([c for c in n if c in "1478"])

print(r)
