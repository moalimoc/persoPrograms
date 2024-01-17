from itertools import product
L = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
n = len(L)

def indice(n):
    tup = list(product(*(n*[range(0, n)])))
    s = []
    for i in tup:
        if i[0] != 0:
            s.append(i)
            
        k = len(i) -1 
        l = 0

        for j in i:
            if j > l:
                s.append(i)
                break
            l += 1

        for j in range(k):
            if i[j+1] - i[j] > 1 or i[j+1] < i[j]:
                s.append(i)
                break
                

    for x in range(len(s)):
        if s[x] in tup:
            tup.remove(s[x])
    
    return tup


def somme1(L):
    somme = 0
    k = len(L)
    Lis = indice(k)
    x = len(Lis) -1
    
    while x != 0:
        som = 0
        for i in range(k):
            j = Lis[x][i]
            som += L[i][j]
        x -= 1

        if som > somme:
            somme = som

    return somme


def ligne_suivante(L1, L2):
    L = L1
    L[0] += L2[0]
    L[-1] += L2[-1]
    for i in range (1, len(L)-1):
        L[i] += max(L2[i-1], L2[i])
    return L

l = [12, 14, 13]
k = [8, 5, 9, 3]

def somme2(L):
    somme = 0
    L = ligne_suivante(k, l)
    for i in L:
        if i > somme:
            somme = i
    return somme


print(somme2(L))

        
    
