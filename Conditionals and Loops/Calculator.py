while True:

    n1 = int(input())

    if n1 == 1:
        n2 = int(input())
        n3 = int(input())
        print(n2+n3)
    elif n1 == 2:
        n2 = int(input())
        n3 = int(input())
        print(n2-n3)
    elif n1 == 3:
        n2 = int(input())
        n3 = int(input())
        print(n2*n3)
    elif n1 == 4:
        n2 = int(input())
        n3 = int(input())
        print(n2//n3)
    elif n1 == 5:
        n2 = int(input())
        n3 = int(input())
        print(n2 % n3)
    elif n1 == 6:
        break
    else:
        print('Invalid Operation')
