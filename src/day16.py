#!/snap/bin/pypy3

file = open("../data/day16.txt", "rt")
data = "".join([f"{int(x,16):04b}" for x in file.read().strip()])
file.close()

part2 = True

def n_bits(string, position, n):
	return string[position:position+n], position+n

def eval(string, position):
	version, position = n_bits(string, position, 3)
	version = int(version, 2)
	type, position = n_bits(string, position, 3)
	type = int(type, 2)
	if type == 4:
		more, position = n_bits(string, position, 1)
		literal_value, position = n_bits(string, position, 4)
		while more == "1":
			more, position = n_bits(string, position, 1)
			v, position = n_bits(string, position, 4)
			literal_value += v
		literal_value = int(literal_value, 2)
		if part2:
			r = literal_value
		else:
			r = version
		return r, position
	else:
		sub_flag, position = n_bits(string, position, 1)
		nb = 11 if sub_flag == "1" else 15
		num, position = n_bits(string, position, nb)
		num = int(num, 2)
		subs = []
		if sub_flag == "1":
			for i in range(num):
				v, position = eval(string, position)
				subs.append(v)
		else:
			end_position = position + num
			while position < end_position:
				v, position = eval(string, position)
				subs.append(v)
		if part2:
			if type == 0:
				r = sum(subs)
			elif type == 1:
				r = 1
				for s in subs:
					r *= s
			elif type == 2:
				r = min(subs)
			elif type == 3:
				r = max(subs)
			elif type == 5:
				r = 1 if subs[0] > subs[1] else 0
			elif type == 6:
				r = 1 if subs[0] < subs[1] else 0
			elif type == 7:
				r = 1 if subs[0] == subs[1] else 0
		else:
			r = version + sum(subs)
		return r, position

print(eval(data, 0)[0])
