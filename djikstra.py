from math import inf

def cle_val_min(dico):
    mini = inf
    for i in dico:
        if dico[i] < mini:
            mini = dico[i]
            cle_min = i
    return cle_min


def dijkstra(graphe, depart, arrivee):
    dsel = {}
    dpar = {}
    dmarq = {}
    
    for cle in graphe:
        dmarq[cle] = inf
    dmarq[depart] = 0

    while arrivee not in dsel:
        s_min = cle_val_min(dmarq)
        dsel[s_min] = dmarq[s_min]
        for sommet in graphe[s_min]:
            if not sommet in dsel:
                distance = dmarq[s_min] + graphe[s_min][sommet]
                if distance < dmarq[sommet]:
                    dmarq[sommet] = distance
                    dpar[sommet] = s_min
        del dmarq[s_min]
        
    return dsel, dpar, dmarq


                
g = {'A': {'B': 15, 'C': 4}, 'B': {'E': 5}, 'C': {'E': 17, 'D': 2}, 'D':{'E': 30}, 'E' : {}}
print(dijkstra(g, 'A', 'E'))
