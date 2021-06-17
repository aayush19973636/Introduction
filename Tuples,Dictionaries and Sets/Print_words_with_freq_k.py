s = 'this string is having many many word word'
k =3 
def printK(s,k):
    words = s.split()
    d = {}
    for w in words:
        d[w] = d.get(w,0) + 1
    for w in words:
        if d[w] == k:
            print(w)
printK(s,k)

    
