#!/snap/bin/pypy3

file = open("../data/day22.txt", "rt")
data = [x.split(' ') for x in file.read().split('\n') if x != '']
file.close()

part2 = True

def intersection(x1,x2,y1,y2,z1,z2,xx1,xx2,yy1,yy2,zz1,zz2):
	left_x = max(x1,xx1)
	right_x = min(x2,xx2)
	left_y = max(y1,yy1)
	right_y = min(y2,yy2)
	left_z = max(z1,zz1)
	right_z = min(z2,zz2)
	if left_x <= right_x and left_y <= right_y and left_z <=  right_z:
		return left_x, right_x, left_y, right_y, left_z, right_z
	return None

cubes = set()

for state,coords in data:
	coords = [tuple([int(y) for y in x[2:].split('..')]) for x in coords.split(',')]
	x1,x2 = coords[0]
	y1,y2 = coords[1]
	z1,z2 = coords[2]
	if not part2 and (x1 < -50 or x2 > 50 or y1 < -50 or y2 > 50 or z1 < -50 or z2 > 50):
		break
	new_cubes = set()
	for (xx1,xx2),(yy1,yy2),(zz1,zz2) in cubes:
		it = intersection(x1,x2,y1,y2,z1,z2,xx1,xx2,yy1,yy2,zz1,zz2)
		if it == None:
			new_cubes.add(((xx1,xx2),(yy1,yy2),(zz1,zz2)))
			continue
		if it == (xx1,xx2,yy1,yy2,zz1,zz2):
			continue
		x_range = []
		if x1 < xx1 and x2 > xx2:
			x_range.append((xx1,xx2))
		elif x1 < xx1:
			x_range.append((xx1,x2))
			if x2 < xx2:
				x_range.append((x2+1,xx2))
		elif x2 > xx2:
			if xx1 < x1:
				x_range.append((xx1,x1-1))
			x_range.append((x1,xx2))
		else:
			if xx1 < x1:
				x_range.append((xx1,x1-1))
			x_range.append((x1,x2))
			if x2 < xx2:
				x_range.append((x2+1,xx2))
		y_range = []
		if y1 < yy1 and y2 > yy2:
			y_range.append((yy1,yy2))
		elif y1 < yy1:
			y_range.append((yy1,y2))
			if y2 < yy2:
				y_range.append((y2+1,yy2))
		elif y2 > yy2:
			if yy1 < y1:
				y_range.append((yy1,y1-1))
			y_range.append((y1,yy2))
		else:
			if yy1 < y1:
				y_range.append((yy1,y1-1))
			y_range.append((y1,y2))
			if y2 < yy2:
				y_range.append((y2+1,yy2))
		z_range = []
		if z1 < zz1 and z2 > zz2:
			z_range.append((zz1,zz2))
		elif z1 < zz1:
			z_range.append((zz1,z2))
			if z2 < zz2:
				z_range.append((z2+1,zz2))
		elif z2 > zz2:
			if zz1 < z1:
				z_range.append((zz1,z1-1))
			z_range.append((z1,zz2))
		else:
			if zz1 < z1:
				z_range.append((zz1,z1-1))
			z_range.append((z1,z2))
			if z2 < zz2:
				z_range.append((z2+1,zz2))
		for i in range(len(x_range)):
			for j in range(len(y_range)):
				for k in range(len(z_range)):
					xx1 = x_range[i][0]
					xx2 = x_range[i][1]
					yy1 = y_range[j][0]
					yy2 = y_range[j][1]
					zz1 = z_range[k][0]
					zz2 = z_range[k][1]
					if intersection(x1,x2,y1,y2,z1,z2,xx1,xx2,yy1,yy2,zz1,zz2) != None:
						continue
					new_cubes.add((x_range[i],y_range[j],z_range[k]))
	if state == 'on':
		new_cubes.add(((x1,x2),(y1,y2),(z1,z2)))
	cubes = new_cubes

r = 0

for (x1,x2),(y1,y2),(z1,z2) in cubes:
	r += (x2-x1+1)*(y2-y1+1)*(z2-z1+1)

# 1165737675582132


print(r)
