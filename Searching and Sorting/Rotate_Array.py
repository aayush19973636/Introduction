from sys import stdin


def rotate(arr, n, d):
    # Solution 1
    temp = []

    i = 0

    while i < d:
        temp.append(arr[i])
        i += 1
    i = 0

    while d < n:
        arr[i] = arr[d]
        i += 1
        d += 1
    arr[:] = arr[: i] + temp
    return arr
    
    # Solution 2
    # for i in range(d):
    #     temp = arr[0]
    #     for i in range(n-1):
    #         arr[i] = arr[i+1]
    #     arr[n-1] = temp

    # Taking Input Using Fats I/O


def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)

    t -= 1
