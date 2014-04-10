def Niveau(vertex,edges):
    #edges: 0:nb, 1:name, 2:type, 3:start, 4:arrival, 5:time
    r = 'y'
    while r == 'y':
        to_pop = []
        level = raw_input("\nWhat kind of piste do you want to avoid? (V,B,R,N,KL,SURF,TPH,TC,TSD,TK,TS,BUS) ")
        for e in edges:
            if edges[e][2] == level:
                to_pop.append(e)
        for e in to_pop:
            edges.pop(e)
        r = raw_input("\nDo you want to avoid another kind of pist? (y for yes) ")
        
    source = raw_input("\nWhat is your starting point? ")
    visited  = DFS(edges,source,[])
    visited = FormatDFS(vertex, visited)
    print "\nYou can reach the following points:"
    for v in visited:
        print v
    

def DFS(edges, source, visited):
    visited.append(source)
    for e in edges:
        if edges[e][3] == source and edges[e][4] not in visited:
            visited = DFS(edges, edges[e][4], visited)
    return visited

def FormatDFS(vertex,visited):
    format = []
    for v in visited:
        format.append(vertex[int(v)][1])
    return format
