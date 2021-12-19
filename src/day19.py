#!/snap/bin/pypy3

file = open("../data/day19.txt", "rt")
data = [x.strip() for x in file.read().strip().split('\n\n') if x != '']
file.close()

part2 = True
r = 0

scanners = {}

for d in data:
	s = []
	for i,l in enumerate(d.split('\n')):
		if i == 0:
			n = l.replace('--- ','').replace(' ---','')
		else:
			s.append(tuple([int(x) for x in l.split(',')]))
	scanners[n] = s

transforms = [(i1,i2,i3,s1,s2,s3)
	for i1,i2,i3 in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
	for s1 in [1,-1] for s2 in [1,-1] for s3 in [1,-1]]

positions = {'scanner 0' : (0,0,0)}

names = [(n1,n2) for n1 in scanners.keys() for n2 in scanners.keys() if n1 != n2]

while len(positions) != len(scanners):
	for n1,n2 in names:
		if n1 not in positions or n2 in positions:
			continue
		sc1 = scanners[n1]
		sc2 = scanners[n2]
		for i1,i2,i3,s1,s2,s3 in transforms:
			tsc2 = []
			for sl in sc2:
				tsc2.append((s1*sl[i1],s2*sl[i2],s3*sl[i3]))
			distances = {}
			match = False
			for x1,y1,z1 in sc1:
				for x2,y2,z2 in tsc2:
					dist = (x2-x1,y2-y1,z2-z1)
					cnt = distances[dist] + 1 if dist in distances else 1
					if cnt >= 12:
						match = True
						break
					else:
						distances[dist] = cnt
				if match:
					break
			if match:
				npx,npy,npz = positions[n1]
				dx, dy, dz = dist
				positions[n2] = (npx+dx,npy+dy,npz+dz)
				scanners[n2] = tsc2
				break

if part2:
	max_distance = float('-inf')
	for n1, n2 in names:
		px1,py1,pz1 = positions[n1]
		px2,py2,pz2 = positions[n2]
		dist = abs(px2-px1)+abs(py2-py1)+abs(pz2-pz1)
		max_distance = max(max_distance, dist)
	print(max_distance)
else:
	points = set()
	for n,s in scanners.items():
		dx, dy, dz = positions[n]
		for x,y,z in s:
			points.add((x-dx,y-dy,z-dz))
	print(len(points))
