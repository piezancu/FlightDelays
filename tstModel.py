import networkx as nx

from model.model import Model

mymodel = Model()
mymodel.buildGraph(5)
mymodel.printGraphDetails()

v0 = mymodel.getAllNodes()[0]
connessa = list(nx.node_connected_component(mymodel._grafo, v0))

v1 = connessa[10]

pathD = mymodel.trovaCamminoDijkstra(v0, v1)
pathBFS = mymodel.trovaCamminoBFS(v0, v1)
pathDFS = mymodel.trovaCamminoDFS(v0, v1)

print("------------------------")
print("Metodo di Dijkstra") # mi da il cammino di costo minimo
print(*pathD, sep="\n")
print("------------------------")
print("Metodo albero Breath First") # mi da il cammino con meno nodi che pesa di più (?)
print(*pathBFS, sep="\n")
print("------------------------")
print("Metodo albero Depth First") # mi da il cammino più lungo (?)
print(*pathDFS, sep="\n")

