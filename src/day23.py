#!/snap/bin/pypy3

import sys
from itertools import permutations

sys.setrecursionlimit(1000000)

part2 = True
r = 0

to_positions = [(0,0), (1,0), (3,0), (5,0), (7,0), (9,0), (10,0)]

y_max = 4 if part2 else 2

return_positions = {}

pA = []
pB = []
pC = []
pD = []

for y in range(0,y_max):
	lbl = 'A'+str(y+1)
	return_positions[lbl] = pA
	pA.append((2,y+1))
	lbl = 'B'+str(y+1)
	return_positions[lbl] = pB
	pB.append((4,y+1))
	lbl = 'C'+str(y+1)
	return_positions[lbl] = pC
	pC.append((6,y+1))
	lbl = 'D'+str(y+1)
	return_positions[lbl] = pD
	pD.append((8,y+1))

# Test:
#if part2:
#	state = { 'B1' : (2,1), 'A1' : (2,4), 'C1' : (4,1), 'D1' : (4,4), 'B2': (6,1), 'C2' : (6,4), 'D2': (8,1), 'A2' : (8,4)}
#else:
#	state = { 'B1' : (2,1), 'A1' : (2,2), 'C1' : (4,1), 'D1' : (4,2), 'B2': (6,1), 'C2' : (6,2), 'D2': (8,1), 'A2' : (8,2)}

if part2:
	state = { 'B1' : (2,1), 'C1' : (2,4), 'B2' : (4,1), 'A1' : (4,4), 'D1': (6,1), 'D2' : (6,4), 'A2': (8,1), 'C2' : (8,4)}
else:
	state = { 'B1' : (2,1), 'C1' : (2,2), 'B2' : (4,1), 'A1' : (4,2), 'D1': (6,1), 'D2' : (6,2), 'A2': (8,1), 'C2' : (8,2)}

part2_fold = { 'D3' : (2,2), 'D4' : (2,3), 'C3' : (4,2), 'B3' : (4,3), 'B4': (6,2), 'A3' : (6,3), 'A4': (8,2), 'C4' : (8,3)}
if part2:
	for k,v in part2_fold.items():
		state[k] = v

yA = []
yB = []
yC = []
yD = []
for p in permutations([str(y+1) for y in range(y_max)]):
	ya = ""
	yb = ""
	yc = ""
	yd = ""
	for j in p:
		ya += '2'+j
		yb += '4'+j
		yc += '6'+j
		yd += '8'+j
	yA.append(ya)
	yB.append(yb)
	yC.append(yc)
	yD.append(yd)

final_states = { a+b+c+d for a in yA for b in yB for c in yC for d in yD }

def move_cost(it):
	if it[0] == 'A':
		return 1
	if it[0] == 'B':
		return 10
	if it[0] == 'C':
		return 100
	if it[0] == 'D':
		return 1000

def state_to_str(s):
	r = ""
	for k in sorted(s.keys()):
		r += str(s[k][0])+str(s[k][1])
	return r

costs = {}

def other_its(it):
	ltr = it[0]
	nums = [str(y+1) for y in range(y_max)]
	nums.remove(it[1])
	return [ltr+n for n in nums]

def search(s,c):
		ss = state_to_str(s)
		if ss in costs and costs[ss] <= c:
			return
		costs[ss] = c
		if ss in final_states:
			return
		for it,pos in s.items():
			rp = return_positions[it]
			if pos in to_positions:
				for dx,dy in rp:
					if dy<y_max and len([oit for oit in other_its(it) if s[oit][0] == dx]) != y_max-dy:
						continue
					pt = path(dx,dy,pos[0],pos[1])
					pt.remove((pos[0],pos[1]))
					occupied = [yy for xx,yy in s.items() if xx != it and yy in pt]
					if len(occupied) > 0:
						continue
					ns = s.copy()
					ns[it] = (dx,dy)
					search(ns, c+move_cost(it)*len(pt))
			else:
				if pos in rp:
					rpx = pos[0]
					rpy = pos[1]
					belows = [(rpx,rrpy) for rrpy in range(rpy+1,y_max+2)]
					oits = other_its(it)
					if len([k for k in s.keys() if s[k] in belows and k not in oits]) == 0:
						continue
				for dx,dy in to_positions:
					pt = path(dx,dy,pos[0],pos[1])
					pt.remove((pos[0],pos[1]))
					occupied = [yy for xx,yy in s.items() if xx != it and yy in pt]
					if len(occupied) > 0:
						continue
					ns = s.copy()
					ns[it] = (dx,dy)
					search(ns, c+move_cost(it)*len(pt))

def path(x0,y0,x1,y1):
	if y0 > y1:
		x0, x1 = x1, x0
		y0, y1 = y1, y0
	assert y0 == 0
	r = []
	for i in range(min(x0,x1),max(x0,x1)+1):
		r.append((i,y0))
		if i == x1:
			for j in range(y0+1,y1+1):
				r.append((i,j))
	return r

search(state,0)

print(min([c for s,c in costs.items() if s in final_states]))
