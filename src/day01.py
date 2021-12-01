#!/snap/bin/pypy3

file = open("../data/day01.txt", "rt")
data = [int(x) for x in file.read().split('\n') if x != '']
file.close()

part2 = True
r = 0

prev = data[0]
if part2:
	prev += (data[1] + data[2])

for i in range(3 if part2 else 1, len(data)):
	d = data[i]
	if part2:
		d += data[i-1] + data[i-2]
	if d > prev:
		r += 1
	prev = d

print(r)
