from collections import defaultdict

from heapq import heappush, heappop

def dijkstra(G, startingNode):
	visited = set()
	parentsMap = {}
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heappush(pq, (0, startingNode))

	while pq:
		# go greedily by always extending the shorter cost nodes first
		_, node = heappop(pq)
		visited.add(node)
		# exit if target

		for adjNode, weight in G[node].items():
			if adjNode in visited:
				continue

			newCost = nodeCosts[node] + weight
			if nodeCosts[adjNode] > newCost:
				parentsMap[adjNode] = node
				nodeCosts[adjNode] = newCost
				heappush(pq, (newCost, adjNode))

	return parentsMap, nodeCosts
