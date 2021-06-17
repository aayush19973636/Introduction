
from sys import stdin

def arrayRotateCheck(arr, n):
    #Your code goes here
    # Find the index of minimum element
    min = arr[0]

    for i in range(n):
        if min > arr[i]:
            min = arr[i]
            min_index = i
    return min_index



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1