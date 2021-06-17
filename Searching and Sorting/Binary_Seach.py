from sys import stdin


def binarySearch(arr, n, x):
    #Your code goes here
    start = 0
    end = len(arr) - 1
    

    while start <= end:
        middle = (start + end)//2

        if arr[middle] < x:
            start = middle + 1
        elif arr[middle] > x: 
            end = middle - 1
        else:
            arr[middle] = x
            return middle
    return -1


    #Taking Input Using Fast I/O


def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0:

    x = int(input().strip())
    print(binarySearch(arr, n, x))

    t -= 1
