
def FloydWarshall(vertex,edges):
#edges: 0:nb, 1:name, 2:type, 3:start, 4:arrival, 5:time
    shortestPath =[]
    succ = []
    n = len(vertex)
    for i in range(0, n):
        l = []
        s = []
        for j in range(0, n):
            s.append(-1)
            if i != j:
                l.append(float('inf'))
            else:
                l.append(0)
        shortestPath.append(list(l))
        succ.append(list(s))

    for k in edges:
        e = edges[k]
        if int(e[5]) < shortestPath[int(e[3])-1][int(e[4])-1]:
            shortestPath[int(e[3])-1][int(e[4])-1] = int(e[5])

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if shortestPath[i][k] + shortestPath[k][j] < shortestPath[i][j]:
                    shortestPath[i][j] = shortestPath[i][k] + shortestPath[k][j]
                    succ[i][j] = k+1
   
                    
    start = int(raw_input("Choose the starting point: "))
    stop = int(raw_input("Choose the starting point: "))
    datas = {'dist': shortestPath, 'succ': succ}
    pathv = [start] + Path(datas, start, stop) + [stop]#contain only the vertex
    path = PathForm(edges,vertex,pathv) #contain name of vertex and edges   
    print ""
    print path
    
    former = -1
    time = 0
    for p in pathv:
        short = float('inf')
        if former != -1:
            for e in edges:
                if int(edges[e][3]) == former and int(edges[e][4]) == p and edges[e][5] < short:
                    short = edges[e][5] 
            time += short
        former = p

    print "This trip takes " + str(int(time/3600)) + " hours, " + str(int((time/60)%60)) + " minutes and " + str(int((time%60))) + " seconds"
    


def Path(datas, start, stop):
    if datas['dist'][start-1][stop-1] == float('inf'):
        return [] #No path between start and stop
    else:
        interm = datas['succ'][start-1][stop-1]
        if interm == -1:
            return []
        else:
            return Path(datas,start,interm) + [interm] + Path(datas, interm, stop)



def PathForm(edges, vertex, path):
    formedpath = ""
    former = -1
    for p in path:
        short = float('inf')
        edge = ""
        if former != -1:
            for e in edges:
                if int(edges[e][3]) == former and int(edges[e][4]) == p and edges[e][5] < short :
                    edge = edges[e][1]
                    short = edges[e][5]
            formedpath = formedpath + "->" + " " + edge + " " + "->" + " "

        for v in vertex:
            if v == p:
                formedpath = formedpath + vertex[v][1] + " "
        former = p
    return formedpath

