n = int(input())
result = 0
while n > 0:
    a = n % 10
    result = result*10 + a
    n = n//10
print(result)
