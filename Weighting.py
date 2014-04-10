def Weighting(vertex, edges):
    time = {}
    options = { 'V': green,
                'B': blue,
                'R': red,
                'N': black,
                'KL': track,
                'SURF': surf,
                'TPH': tph,
                'TC': tc,
                'TSD': tsd,
                'TS': tsk,
                'TK': tsk,
                }

    for i in edges:
        start = int(edges[i][3])
        arrival = int(edges[i][4])
        slope = abs(int(vertex[start][2]) - int(vertex[arrival][2]))
        if edges[i][2] == 'BUS':
            if vertex[arrival][1] == "arc1800" or vertex[start][1] == "arc1800":
                edges[i].append(30*60)
            elif vertex[arrival][1] == "arc2000" or vertex[start][1] == "arc2000":
                edges[i].append(40*60)
        else:            
            edges[i].append(round(options[edges[i][2]](slope),3))
            
 
    return edges


def green(s):
    return (5*60*(float(s)/100))

def blue(s):
    return (4*60*(float(s)/100))

def red(s):
    return (3*60*(float(s)/100)) 
def black(s):
    return (2*60*(float(s)/100))

def track(s):
    return (10*(float(s)/100))
    
def surf(s):
    return (10*60*(float(s)/100))

def tph(s):
    return ((4*60) + (2*60*(float(s)/100)))

def tc(s):
    return ((2*60) + (3*60*(float(s)/100)))

def tsd(s):
    return ((1*60) + (3*60*(float(s)/100)))

def tsk(s):
    return ((1*60) + (4*60*(float(s)/100)))
