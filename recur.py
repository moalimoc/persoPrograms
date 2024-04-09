from time import perf_counter


def f(n):
    if n == 0:
        return 1
    return f(n-1)*n

def somme(L):
    l = len(L)
    if l == 0:
        return 0
    return somme(L[0:-1])+L[-1]

def renverse(L):
    if len(L) == 1:
        return L
    return [L[-1]]+renverse(L[:-1])

def palindrome(chaine):
    if len(chaine) <= 1:
        return True
    if chaine[0] != chaine[-1]:
        return False
    return palindrome(chaine[1:-1])


L = [1, 2, 3, 4]
c = "ali"
c2 = "kayak"
c3 = ""

def pascal1(n, k):
    if k > n:
        return 0
    if k == n or k == 0:
        return 1
    return pascale1(n-1, k-1) + pascale1(n-1, k)

def pascal2(n, k): #complexity O(k)
    if k > n:
        return 0
    if k == n or k == 0:
        return 1
    return int((n/k)*pascal2(n-1, k-1)) #ou bien (et c'est mieux): return (n*pascal1(n-1, k-1))//k


def ligne_suivante(L):
    l = [1]
    for i in range(len(L)-1):
        l.append(L[i]+L[i+1])
    l.append(1)

    return l

def pascal3(n, k):
    if k > n:
        return 0
    lis = [1]
    for i in range(n):
        lis = ligne_suivante(lis)
    return lis[k]

memoire = {}

def pascal4(n, k):
    if k > n:
        return 0
    if (n, k) in memoire:
        return memoire[n, k]
    if 0 < k < n:
        v = pascal4(n-1, k) + pascal4(n-1, k-1)
    else:
        v = 1
    memoire[(n, k)] = v
    return v


#exo 11
def expo1(x, n): #linear complexity O(n)
    c = 1
    for k in range(n):
        c *= x
    return c

def expo2(x, n): #linear complexity O(n)
    if n == 0:
        return 1
    if x == 0 or x == 1:
        return x
    return x * expo2(x, n-1)



def expo4(x, n): #complexity O(log(n))
    if n == 0:
        return 1
    a = expo4(x, n//2)
    if n % 2 == 0:
        return a * a
    return x * a * a

    
def expo3(x, n):  #complexity O(log(n))
    if n == 0:
        return 1
    a = expo3(x*x, n//2)
    if n % 2 == 0:
        return a
    else:
        return x * a
    


