n = int(input())
i = 1

while i <= n:
    spaces = 1

    while spaces <= n-i:
        print(" ", end="")
        spaces += 1

    stars = 1
    while stars <= i:
        print(stars, end="")
        stars += 1
    print()
    i += 1
