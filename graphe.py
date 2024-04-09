from collections import deque
from numpy.linalg import transpose

def parcours_profondeur_recur(graphe, u):
    L_visites.append(u)
    for voisin in graphe[u]:
        if not voisin in L_visites:
            parcours_profondeur_recur(graphe, voisin)


L_visites = []
d = {
    1: [2, 6],
     2:[1, 3, 4, 7],
     6:[1, 7, 8],
     3: [2, 5],
     7: [2, 6, 9],
     5: [3, 9],
     4: [2, 9],
     8: [6, 9],
     9: [4, 5, 7, 8]
    }


def parcours_profondeur(graphe, u):
    L_visit = [u]
    p = [u]
    while len(p) > 0:
        sommet = p[-1]
        L_v_n = [k for k in graphe[sommet] if not k in L_visit]
        if len(L_v_n) > 0:
            v = L_v_n[0]
            L_visit.append(v)
            p.append(v)
        else:
            p.pop()
    return L_visit

def parcours_largeur(graphe, u):
    L_visit = [u]
    f = [u]
    while len(f) > 0:
        sommet = f[0]
        L_v_n = [k for k in graphe[sommet] if not k in L_visit]
        if len(L_v_n) > 0:
            v = L_v_n[0]
            L_visit.append(v)
            f.append(v)
        else:
            f.pop(0)
    return L_visit

def existCh(graphe, u, v):
    L_visit = [u]
    f = [u]
    while len(f) > 0 and not v in L_visit:
        sommet = f[0]
        L_v_n = [k for k in graphe[sommet] if not k in L_visit]
        if len(L_v_n) > 0:
            w = L_v_n[0]
            L_visit.append(w)
            f.append(w)
        else:
            f.pop(0)
    return v in L_visit

def matrcAdj(matriceAdj, u, v):
    L_visit = [u]
    f = [u]
    while len(f) > 0 and not v in L_visit:
        sommet = f[0]
        M = [i+1 for i in range(len(matriceAdj[sommet-1]) if matriceAdj[sommet-1][i] == 1]
        L_v_n = [k for k in M if not k in L_visit]
        if len(L_v_n) > 0:
            w = L_v_n[0]
            L_visit.append(w)
            f.append(w)
        else:
            f.pop(0)
    return v in L_visit

def connecte1(matriceAdj):
    n = len(matriceAdj)
    for u in range(1, n):
        for v in range(u+1, n+1):
            if not existCh(matriceAdj, u, v):
                return False
    return True

def connecte2(matriceAdj):
    n = len(matriceAdj)
    for u in range(1, n+1):
        for v in range(1, n+1):
            if not existCh(matriceAdj, u, v) and u != v:
                return False
    return True

    
print(existCh(d, 1, 91))
print(parcours_largeur(d, 1))
