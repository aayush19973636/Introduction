n = int(input())
i = 1

while i <= n:
    start_char = chr(ord('A')+n-i)
    j = 1
    while j <= i:
        charP = chr(ord(start_char)+j-1)
        print(charP, end="")

        j = j+1
    print()
    i = i+1
