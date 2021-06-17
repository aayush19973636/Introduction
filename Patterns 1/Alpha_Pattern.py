n = int(input())
i = 1

while i <= n:
    start_char = chr(ord('A')+i-1)
    j = 1
    while j <= i:
        charP = chr(ord(start_char))
        print(charP, end="")

        j = j+1
    print()
    i = i+1
