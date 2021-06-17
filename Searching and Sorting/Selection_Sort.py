def selection(arr):
    n = len(arr)

    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if  arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


arr = [1, 6, 3, 2, 4, 5, 8, 0, 9, 7]
selection(arr)
print(arr)
