#!/snap/bin/pypy3

file = open("../data/day03.txt", "rt")
data = [[int(y) for y in list(x)] for x in file.read().split('\n') if x != '']
file.close()

part2 = True

str1 = ""
str2 = ""

if part2:
	new_data1 = data[:]
	p = 0
	while len(new_data1) > 1:
		ones = 0
		zeros = 0
		for d in new_data1:
			if d[p] == 1:
				ones += 1
			else:
				zeros += 1
			to_keep = 1 if ones >= zeros else 0
		new_data1 = [x for x in new_data1 if x[p] == to_keep]
		p += 1
	for c in new_data1[0]:
		str1 += "1" if c == 1 else "0"
	new_data2 = data[:]
	p = 0
	while len(new_data2) > 1:
		ones = 0
		zeros = 0
		for d in new_data2:
			if d[p] == 1:
				ones += 1
			else:
				zeros += 1
			to_keep = 0 if ones >= zeros else 1
		new_data2 = [x for x in new_data2 if x[p] == to_keep]
		p += 1
	for c in new_data2[0]:
		str2 += "1" if c == 1 else "0"
else:
	occ = [0]*12
	l = len(data[0])
	ll = len(data)
	for d in data:
		for i in range(0, l):
			if d[i] == 1:
				occ[i] = occ[i] + 1
	for c in occ:
		str1 += "1" if c > ll/2 else "0"
		str2 += "1" if c < ll/2 else "0"

print(int(str1,2)*int(str2,2))
