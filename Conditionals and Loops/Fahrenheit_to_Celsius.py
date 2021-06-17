s = int(input())
e = int(input())
w = int(input())

while True:
    c = 0

    if s <= e:
        c = (s-32)*5/9
        print(s, int(c))
        s = s+w
    else:
        break
