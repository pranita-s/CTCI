
# TIME -
# SPACE - 

import collections
class Graph:
	
	def __init__(self):
  		self.visited = {}
    	self.edges = collections.defaultdict(list)
        self.answer = False
		self.vertices = []

	def routeNodesDFS(self,node1, node2):
    	if node1 == node2:
        	self.answer = True
        self.visited[node1] = True
        for neighbor in self.edges(node1):
            	if not self.visited[neighbor]:
                	self.dfs(neighbor,node2)
		return self.answer
        
    def initiate(self,g):
		grafV = ['0','1','2','3','4','5']
        for v in grafV:
            self.vertices.append(v)
            self.visited[v]=False
        for e in g:
            self.edges[e[0]].append(e[1])

        print(self.routeNodesDFS('2','5'))


if __name__ == "__main__":
	G= Graph()
    g = graf = [['0', '1'], ['0', '4'], ['0', '5'], ['1', '3'], ['1', '4'], ['2', '1'], ['3', '2'], ['3', '4']]
    G.initiate(g)
