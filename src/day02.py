#!/snap/bin/pypy3

file = open("../data/day02.txt", "rt")
data = [(y[0], int(y[1])) for y in [x.split(' ') for x in file.read().split('\n') if x != '']]
file.close()

part2 = True
distance = 0
depth = 0
aim = 0

for d,steps in data:
	if d == 'down':
		if part2:
			aim += steps
		else:
			depth += steps
	elif d == 'up':
		if part2:
			aim -= steps
		else:
			depth -= steps
	elif d == 'forward':
		distance += steps
		if part2:
			depth += aim * steps

print(distance * depth)
