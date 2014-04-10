from Parsing import ParseVertex
from Parsing import ParseEdges
from Weighting import Weighting
from short import FloydWarshall
from Niveau import Niveau
vertex = {}
edges = {}
time = {}
shortestPath = []

f = open("dataski.txt", 'r')
strplan = f.readlines()

vertex = ParseVertex(strplan)
edges = ParseEdges(strplan)
edges = Weighting(vertex, edges) 
#Datastructure: dict of lists
#vertex: 0:nb, 1:name, 2:altitude
#edges: 0:nb, 1:name, 2:type, 3:start, 4:arrival, 5:time


FloydWarshall(vertex,edges)
print ""
Niveau(vertex,edges)

s = raw_input("Appuyez sur ENTREE pour terminer le programme.")
