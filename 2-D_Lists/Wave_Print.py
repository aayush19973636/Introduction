from sys import stdin


def wavePrint(mat, nRows, mCols):
    #Your code goes here
    for j in range(mCols):
        k = [] #need empty list for reversing the column
        for i in range(nRows):
            if j % 2 == 0:
                print(mat[i][j], end=' ')
            else:
                k.append(mat[i][j])
        k = k[::-1]
        for _ in k:
            print(_, end=" ")

    #Taking Input Using Fast I/O


def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0:

    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1
