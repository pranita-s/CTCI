# TIME - O(V+E)
# SPACE - O(E)

import collections
class Graph:
  
	def __init__(self):
		self.edges = collections.defaultdict(list)
    	self.vertices = collections.defaultdict(int)
	
	def buildOrder(self):
		build_order = []
		q = collections.deque()
		for v in self.vertices:
			if self.vertices[v] == 0:
				q.append(v)
		while q:
			popped = q.popleft()
			build_order.append(popped)
			for neighbor in in self.edges[popped]:
				self.vertices[neighbor] -= 1
				if self.vertices[neighbor] == 0:
					q.append(neighbor)
		
		if len(build_order) < len(self.vertices.keys()):
			return Exception("Cycle has been detected")
		return build_order
			
	
	def createGraph(self,proj,dep
		for p in project:
			self.vertices[p] = 0
		for e in dep:
			self.edges[e[0]].append(e[1])
			self.vertices[e[1]] += 1

    def initiate(self,proj,dep):
        for p in proj:
            self.projects[p] = 0
        for e in dep:
            self.edges[e[0]].append(e[1])
            self.projects[e[1]] += 1
        print(self.buildOrder())

if __name__=='__main__':
    G=Graph()
    projects = ["a", "b", "c", "d", "e", "f","g"]
    dependencies = [("f", "c"), ("f", "b"), ("f", "a"), ("c", "a"), ("b", "a"),("b","e"),("a","e"),("d","g")]
    G.initiate(projects,dependencies)

   
   
  
