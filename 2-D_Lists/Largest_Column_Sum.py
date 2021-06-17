def largestColSum(li):
    row = len(li)
    col = len(li[0])

    maxSum = -1
    maxColIndex = -1

    for i in range(row):
        sum = 0
        for j in range(col):
            sum += li[j][i]
        
        if sum > maxSum:
            maxColIndex = i
            maxSum = sum
    return maxSum, maxColIndex




li = [[1,2,3,4],
     [5,6,70,8],
     [9,10,11,12],
     [13,14,15,160]]

largestSum,largestColIndex = largestColSum(li)
print(largestSum,largestColIndex)