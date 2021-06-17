from sys import stdin


def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    ColStart,RowStart,ColEnd,RowEnd = 0, 0, mCols-1, nRows-1

    while ColStart <= ColEnd and RowStart <= RowEnd:
        for j in range(ColStart, ColEnd+1):
            print(mat[RowStart][j], end=' ')
        RowStart += 1
        if RowStart > RowEnd or ColStart > ColEnd:
            break
        # Print ColEnd
        for i in range(RowStart, RowEnd+1):
            print(mat[i][ColEnd], end=' ')
        ColEnd -= 1
        if RowStart > RowEnd or ColStart > ColEnd:
            break
        for j in range(ColEnd, ColStart-1, -1):
            print(mat[RowEnd][j], end=' ')
        RowEnd -= 1
        if RowStart > RowEnd or ColStart > ColEnd:
            break
        # Print ColStart
        for i in range(RowEnd, RowStart-1, -1):
            print(mat[i][ColStart], end=' ')
        ColStart += 1
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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
