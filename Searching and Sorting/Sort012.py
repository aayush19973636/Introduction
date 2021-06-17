from sys import stdin


def sort012(arr, n):
    #Your code goes here
    lo = 0 #0
    hi = n - 1 #2
    mid = 0 #1

    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi = hi - 1
    return arr



#Taking Input Using Fast I/O


def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0:

    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)

    t -= 1
