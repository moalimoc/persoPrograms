from random import randint
from random import shuffle

def alea_adn(N):
    c = ''
    L = ['A', 'C', 'T', 'G']
    for i in range(N):
        c += L[randint(0, 3)]
    return c

def decoupage_kmer(sequence, k):
    L = []
    for i in range(len(sequence) -(k-1)):
        L.append(sequence[i:i+k])     
    return L

def melange_kmer(L_kmer):
    a = L_kmer.pop()
    shuffle(L_kmer)
    return [a] + L_kmer

N, k = 30, 3
sequence = alea_adn(N)
L_kmer = decoupage_kmer(sequence, 3)

graphe = {i:[] for i in range(len(L_kmer))}

def nom(L_kmer):
    n = len(L_kmer)
    graphe = {i:[] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if L_kmer[i][1:] == L_kmer[j][:-1]:
                graphe[i].append(j)
    return graphe

def hamilton(u):
    parcours.append(u)
    if len(parcours) == n:
        return True
    vois = [k for k in graphe[u] if not k in parcours]
    for v in vois:
        if hamilton(v):
            return True
        else:
            parcours.pop()
    return False
