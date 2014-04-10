
def ParseVertex(strplan):
    vertex = {}
    jac = 0 #iterateur dans la ligne
    jprec = 0 #iterateur place au debut du string
    
    nv = int(strplan[0])
    for i in range(1,nv + 1):
        vertex[i] = []
        jprec = 0
        jac = 0
        for c in strplan[i]:
            if c == '\t':
                if strplan[i][jprec:jac] != "":
                    vertex[i].append(strplan[i][jprec:jac])
                    jprec = jac +1 #so jprec 'jump' over the indication carac '\..'
            jac +=1

    return vertex



        
def ParseEdges(strplan):
    nv = int(strplan[0])
    ned = int(strplan[nv+1])
    edges = {}
    
    for i in range(1,ned + 1):
        edges[i] = []
        jprec = 0
        jac = 0
        for c in strplan[i + nv+1]:
            if c == '\t' or c == '\n':
                if strplan[i + nv+1][jprec:jac] != "":
                    edges[i].append(strplan[i + nv+1][jprec:jac])
                    jprec = jac +1 #so jprec 'jump' over the indication carac '\..'
            jac +=1
    return edges
    
