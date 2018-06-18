
# TIME - O(V+E)
# SPACE - O(E)

import collections
class Graph:

	def __init__(self):
		self.vertices = {}
		self.edges = collections.defaultdict(list)
		self.build_order = []
	
	def dfs(self,v):
		if self.vertices[v] == 'VISITING':
			return False
		if self.vertices[v] == 'UNVISITED':
			self.vertices[v] == 'VISITING'
			for neighbor in self.edges[v]:
				if not self.dfs(neighbor):
					return False
			self.vertices[v] = 'VISITED'
			self.build_order.insert(0,v)
		return True
		
	def buildOrder(self):
		for v in self.vertices.keys():
			if not self.dfs(v):
				return False
		return self.build_order	
	
    def initiate(self,proj,dep):
        for v in proj:
            self.vertices[v]="UNVISITED"
        for e in dep:
            self.edges[e[0]].append(e[1])
        print(self.buildOrder())

if __name__=='__main__':
    G=Graph()
    projects = ["a", "b", "c", "d", "e", "f","g"]
    dependencies = [("f", "c"), ("f", "b"), ("f", "a"), ("c", "a"), ("b", "a"),("b","e"),("a","e"),("d","g")]
    G.initiate(projects,dependencies)
#['f', 'd', 'g', 'b', 'c', 'a', 'e']
#['f', 'd', 'g', 'b', 'c', 'a', 'e']
