
import sys


def duplicateNumber(arr, n):
    # Your code goes here
    for i in range(n):
        j = 0
        while j < n:
            if i != j:
                if arr[i] == arr[j]:
                    return arr[i]
            j += 1

    # Taking Input Using Fast I/O

def takeInput():
    n = int(sys.stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


# main
t = int(sys.stdin.readline().strip())

while t > 0:

    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1
