#!/snap/bin/pypy3

file = open("../data/day24.txt", "rt")
data = [x for x in file.read().split('\n') if x != '']
file.close()

part2 = True

consts1 = []
consts2 = []
consts3 = []

for d in data:
	if d == 'inp w':
		cnt = 0
	if cnt == 4:
		consts3.append(int(d[6:]))
	elif cnt == 5:
		consts1.append(int(d[6:]))
	elif cnt == 15:
		consts2.append(int(d[6:]))
	cnt += 1

rel_pos = {}
max_pos = []
stack = []

for p,c3 in enumerate(consts3):
	if c3 == 1:
		max_pos.append(p)
		stack.append(p)
	else:
		rel_pos[p] = stack.pop()

digits = [x for x in range(1,10)]
if not part2:
	digits.reverse()

r = [0] * 14
for i in range(14):
	if i not in max_pos:
		prev_i = rel_pos[i]
		for old_w in digits:
			w = (consts2[prev_i] + old_w) % 26 + consts1[i]
			if 1 <= w <= 9:
				break
		r[prev_i] = old_w
		r[i] = w

print("".join([str(x) for x in r]))
