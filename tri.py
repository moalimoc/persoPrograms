from random import randint
from time import perf_counter

def tri_bulles(L):
    n = len(L)
    for i in range(1, n):
        for j in range(0, n-1):
            if L[j] > L[j+1]:
                c = L[j]
                L[j] = L[j+1]
                L[j+1] = c
    return L


def tri_casier(L):
    m = min(L)
    n = max(L) - m +1
    k = len(L)
    L_compt = n * [0]
    for i in L:
        L_compt[i-m] += 1
    a, i = 0, 0
    for j in L_compt:
        L[a:a + j] = j * [m+i]
        i += 1
        a += j
    return L

def fusion_moities(Lg, Ld):
    i_g, i_d = 0, 0
    Lfusion = []
    n_g, n_d = len(Lg), len(Ld)
    while i_g < n_g and i_d < n_d:
        if Lg[i_g] <= Ld[i_d]:
            Lfusion.append(Lg[i_g])
            i_g += 1
        else:
            Lfusion.append(Ld[i_d])
            i_d += 1
    if i_g == n_g:
        Lfusion.extend(Ld[i_d:])
    else:
        Lfusion.extend(Lg[i_g:])

    return Lfusion

L = [8, 7, 4, 2, 6, 3, 5]

def tri_fusion(L):
    if len(L) <= 1:
        return L
    Lg = tri_fusion(L[:len(L)//2])
    Ld = tri_fusion(L[len(L)//2:])
    return fusion_moities(Lg, Ld)


def placement_pivot(L):
    n, j = len(L), 0
    p = L[-1]
    for i in range(n-1):
        if L[i] <= p:
            L[i], L[j] = L[j], L[i]
            j += 1
    L[j], L[-1] = L[-1], L[j]
    return j

def tri_rapide(L):
    if len(L) <= 1:
        return L
    j = placement_pivot(L)
    return tri_rapide(L[:j]) + [L[j]] + tri_rapide(L[j+1:])

L1 = [randint(0, 1000) for i in range(100)]

t = perf_counter()
for i in range(100):
    L2 = L1[:]
    tri_bulles(L2)
print('tri_bulles:', perf_counter() -t)

t = perf_counter()
for i in range(100):
    L2 = L1[:]
    tri_casier(L2)
print('tri_casier:', perf_counter() -t)

t = perf_counter()
for i in range(100):
    L2 = L1[:]
    tri_rapide(L2)
print('tri_rapide:', perf_counter() -t)

t = perf_counter()
for i in range(100):
    L2 = L1[:]
    tri_fusion(L2)
print('tri_fusion:', perf_counter() -t)

t = perf_counter()
for i in range(100):
    L2 = L1[:]
    L2.sort()
print('tri_sort:', perf_counter() -t)

