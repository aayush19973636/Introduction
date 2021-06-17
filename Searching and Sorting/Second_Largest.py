from sys import stdin


def secondLargestElement(arr, n):
    #Your code goes here
    largest = second = -2147483648
    for i in range(n):
        largest = max(largest, arr[i])
    
    for i in range(n):
        if arr[i] != largest:
            second = max(second, arr[i])
    return second


    #Taking Input Using Fast I/O


def takeInput():
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#main
t = int(stdin.readline().rstrip())

while t > 0:

    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1
