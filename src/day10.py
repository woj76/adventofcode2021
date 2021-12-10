#!/snap/bin/pypy3

file = open("../data/day10.txt", "rt")
data = [x for x in file.read().split('\n') if x != '']
file.close()

part2 = True
r = [] if part2 else 0

scores = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137, '(' : 1, '[' : 2, '{' : 3, '<' : 4 }

for d in data:
	stack = []
	corrupted = False
	for c in d:
		if c in ['(', '[', '{', '<']:
			stack.append(c)
		else:
			if stack.pop()+c not in ["()", "[]", "{}", "<>"]:
				corrupted = True
				if not part2:
					r += scores[c]
		if corrupted:
			break
	if part2 and not corrupted:
		s = 0
		while stack:
			s = s*5 + scores[stack.pop()]
		if s:
			r.append(s)

if part2:
	r.sort()
	print(r[ len(r) // 2 ])
else:
	print(r)
