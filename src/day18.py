#!/snap/bin/pypy3

file = open("../data/day18.txt", "rt")
data = [x.strip() for x in file.read().split('\n') if x != '']
file.close()

part2 = True

class Tree:
	def __init__(self):
		self.parent = self.left = self.right = self.value = None

	def print(self):
		if self.value != None:
			return f"{self.value}"
		else:
			return f"[{self.left.print()},{self.right.print()}]"

	def h(self):
		if self.value != None:
			return 0
		return 1 + max(self.left.h(), self.right.h())

	def max(self):
		if self.value != None:
			return self.value
		return max(self.left.max(), self.right.max())

def parse_tree(string, pos):
	if string[pos] == '[':
		l,pos = parse_tree(string,pos+1)
		assert string[pos] == ','
		r,pos = parse_tree(string,pos+1)
		assert string[pos] == ']'
		pos += 1
		t = Tree()
		t.left = l
		t.right = r
		t.left.parent = t
		t.right.parent = t
		return t, pos
	else:
		t = Tree()
		t.value = int(string[pos])
		return t, pos+1

def magnitude(t):
	if t.value != None:
		return t.value
	else:
		return 3*magnitude(t.left) + 2*magnitude(t.right)

def search_leftmost_pair(t,d):
	if d == 4 and t.left.value != None and t.right.value != None:
		return t
	r = None
	if t.left.value == None:
		r = search_leftmost_pair(t.left, d+1)
	if r == None and t.right.value == None:
		r = search_leftmost_pair(t.right, d+1)
	return r

def search_leftmost_value(t):
	if t.value != None and t.value >= 10:
		return t
	r = None
	if t.left != None:
		r = search_leftmost_value(t.left)
	if r == None and t.right != None:
		r = search_leftmost_value(t.right)
	return r

def add_tree(t1, t2):
	t = Tree()
	t.left = t1
	t.right = t2
	t.left.parent = t
	t.right.parent = t
	while True:
		if t.h() == 5:
			tt = search_leftmost_pair(t, 0)
			# explode
			lv = tt.left.value
			rv = tt.right.value
			tt.left = tt.right = None
			tt.value = 0
			ttl = tt
			ttt = None
			while ttl.parent != None:
				if ttl.parent.left != ttl:
					ttt = ttl.parent.left
					break
				ttl = ttl.parent
			if ttt != None:
				while ttt.right != None:
					ttt = ttt.right
				ttt.value += lv
			ttr = tt
			ttt = None
			while ttr.parent != None:
				if ttr.parent.right != ttr:
					ttt = ttr.parent.right
					break
				ttr = ttr.parent
			if ttt != None:
				while ttt.left != None:
					ttt = ttt.left
				ttt.value += rv
		elif t.max() >= 10:
			# split
			tt = search_leftmost_value(t)
			tt1 = Tree()
			tt2 = Tree()
			tt1.value = tt.value // 2
			tt2.value = tt.value - tt1.value
			tt.value = None
			tt1.parent = tt
			tt2.parent = tt
			tt.left = tt1
			tt.right = tt2
		else:
			break
	return t

if part2:
	max_magnitude = float('-inf')
	for i,j in [(i,j) for i in range(len(data)) for j in range(len(data)) if i != j]:
		t1,_ = parse_tree(data[i], 0)
		t2,_ = parse_tree(data[j], 0)
		max_magnitude = max(max_magnitude, magnitude(add_tree(t1,t2)))
	print(max_magnitude)
else:
	trees = []
	for d in data:
		t,_ = parse_tree(d, 0)
		trees.append(t)
	while len(trees) > 1:
		t = add_tree(trees[0],trees[1])
		trees = trees[1:]
		trees[0] = t
	print(magnitude(trees[0]))
