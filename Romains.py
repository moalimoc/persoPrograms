def valeursD(lettre):
    d = {}
    d["M"], d ["D"], d["C"], d["L"], d["X"], d["V"], d["I"] = 1000, 500, 100, 50, 10, 5, 1
    return d[lettre]

def romains(s):
    if len(s) == 1:
        return valeursD(s)
    if s[0] > s[1]:
        return valeursD(s[0]) + romains(s[1:])
    else:
        return romains(s[1:]) - valeursD(s[0])
