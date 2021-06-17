from sys import stdin


def merge(arr1, n, arr2, m):
    #Your code goes here
    arr3 = [None]* (n + m)
    i,j,k = 0,0,0

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr3[k] = arr2[j]
            k += 1
            j += 1
    
    while i < n:
        arr3[k] = arr1[i]
        k += 1
        i += 1
    
    while j < m:
        arr3[k] = arr2[j]
        k += 1
        j += 1
    
    return arr3

    #Taking Input Using Fast I/O


def takeInput():
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0:

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
