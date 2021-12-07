#!/snap/bin/pypy3

file = open("../data/day07.txt", "rt")
data = [int(x) for x in file.read().split(',') if x != '']
file.close()

part2 = True

l,h = float('inf'), float('-inf')

for d in data:
	l, h = min(l, d), max(h, d)

min_fuel = float('inf')

for m in range(l, h+1):
	fuel = 0
	for d in data:
		steps = abs(d - m)
		if part2:
			steps = (steps)*(steps+1)//2
		fuel += steps
	min_fuel = min(min_fuel, fuel)

print(min_fuel)
