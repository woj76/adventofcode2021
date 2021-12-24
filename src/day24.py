#!/snap/bin/pypy3

file = open("../data/day24.txt", "rt")
data = [x for x in file.read().split('\n') if x != '']
file.close()

part2 = True

listing = [""] * 18

def expand(d):
	while len(d) < 10:
		d = d + " "
	return d

for d in data:
	if d == 'inp w':
		cnt = 0
	listing[cnt] = listing[cnt] + expand(d)
	cnt += 1

#for l in listing:
#	print(l)

"""
mul x 0
add x z
mod x 26
div z 1		# const3
add x 11	# const1
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6		# const2
mul y x
add z y
"""

def step(w, z, const1, const2, const3):
	x = 0 if w == z % 26 + const1 else 1
	z = z // const3
	# const3 == 1 -> leave untouched (keep building)
	# const3 == 26 -> revert to previous
	z = z*(25*x + 1) + x*(w + const2)
	return z

consts1 = [11, 13, 15, -8, 13, 15, -11, -4, -15, 14, 14, -1, -8, -14]
consts2 = [6,  14, 14, 10,  9, 12,   8, 13,  12,  6,  9, 15,  4,  10]
consts3 = [1,  1,   1, 26,  1,  1,  26, 26,  26,  1,  1, 26,  26, 26]

# These are input specific and could be calculated from the
# consts3 array above

rel_pos = {3 : 2, 6 : 5,  7 : 4, 8 : 1, 11 : 10, 12 : 9, 13 : 0}
max_pos = [0, 1, 2, 4, 5, 9, 10]

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
