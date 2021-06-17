from sys import stdin


def sumOfTwoArrays(arr1, n, arr2, m, output):
    #Your code goes here
    carry = 0
    i = n-1
    j = m-1
    k = max(n,m) # To find which array is larger in size

    while i >= 0 and j>=0:
        total = arr1[i] + arr2[j] + carry
        output[k] = total % 10
        carry = total//10
        i -=1
        j -=1
        k -=1
    
    while i>= 0:
        total = arr1[i]+carry
        output[k] = total % 10
        carry = total//10
        i -= 1
        k -= 1
    
    while j >= 0:
        total = arr2[j]+carry
        output[k] = total % 10
        carry = total//10
        j -= 1
        k -= 1

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
    arr1, n = takeInput()
    arr2, m = takeInput()

    outputSize = (1 + max(n, m))
    output = outputSize * [0]

    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)

    t -= 1
