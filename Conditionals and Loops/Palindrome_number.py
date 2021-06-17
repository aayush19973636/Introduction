num = int(input())
temp = num
rev = 0

while num > 0:
    a = num % 10
    rev = rev*10 + a
    num = num//10

if temp == rev:
    print('true')
else:
    print('false')
