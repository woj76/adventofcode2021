#!/snap/bin/pypy3

file = open("../data/day06.txt", "rt")
data = [int(x) for x in file.read().split(',') if x != '']
file.close()

part2 = True
population = [0] * 9

for d in data:
	population[d] += 1

for _ in range(256 if part2 else 80):
	new_eights = new_six = population[0]
	for i in range(8):
		population[i] = population[i+1]
	population[6] += new_six
	population[8] = new_eights

print(sum(population))
