import sys

def merge(p,q):
    i = 0
    j = 0
    r = []
    #print(f"receive{p} and {q}")
    while i < len(p) or j < len(q):
        if i<len(p) and j<len(q):
            if p[i]<q[j]:
                r = r + [p[i]]
                i = i + 1
            else:
                r = r + [q[j]]
                j = j + 1
        elif i>=len(p):
            r = r + [q[j]]
            j = j + 1
            #r = r + [q[j:]]
            #break
        else:
            r = r + [p[i]]
            i = i + 1
            #r = r + [p[i:]]
            #break
    #print(f"merge finish{r}")
    return r
def mergesort(a):
    n = len(a)
    print(n)
    if n == 1 :
        return a
    else:
        p = mergesort(a[:n//2])
        q = mergesort(a[n//2:])
        print(f"merge {p} and {q}")
        return merge(p,q)
"""
def startsort(array):
    a=array.copy()
    a = mergesort(a)
    return a
"""
a = [5,9,4,0,7,3,1,8]
print(mergesort(a))
