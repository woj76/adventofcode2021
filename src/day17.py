#!/snap/bin/pypy3

part2 = True

# Too lazy to parse the input file :/
xt_min, xt_max = 137,171
yt_min, yt_max = -98,-73

xvs = {}

# Narrow down candidates for initial x velocity

for xvi in range(1, xt_max+1):
	x = 0
	i = 0
	xv = xvi
	while True:
		x += xv
		xv -= 1
		i += 1
		if x > xt_max or xv == 0:
			break
		if x >= xt_min and x <= xt_max:
			if i in xvs:
				xvs[i].append(xvi)
			else:
				xvs[i] = [xvi]

if part2:
	ip = set()
else:
	max_y = float('-inf')

for steps in xvs:
	# Guessing the correct range for y initial velocity
	# caused me one more wrong answer this year :(
	# 10 seems to be arbitrary and will not work for all
	# inputs!
	for yvi in range(yt_min,10*steps):
		for xvi in xvs[steps]:
			xv, yv, x, y = xvi, yvi, 0, 0
			local_max_y = float('-inf')
			while True:
				x += xv
				y += yv
				if not part2:
					local_max_y = max(local_max_y, y)
				if xv > 0:
					xv -= 1
				yv -= 1
				if xt_min <= x <= xt_max and yt_min <= y <= yt_max:
					if part2:
						ip.add((xvi,yvi))
					else:
						max_y = max(max_y, local_max_y)
				if y < yt_min:
					break;

if part2:
	print(len(ip))
else:
	print(max_y)
