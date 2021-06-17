def order(x):
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
    return n

def armstrong(x):
    n = order(x)
    temp = x
    sum1 = 0

    while temp != 0:
        r = temp % 10
        sum1 = sum1 + pow(r, n)
        temp = temp//10
    return sum1==x

x = int(input())
Armstrong = armstrong(x)
if (Armstrong):
    print("true")
else:
    print("false")

# num = int(input("Enter a number: "))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# # display the result
# if num == sum:
#    print(num, "is an Armstrong number")
# else:
#    print(num, "is not an Armstrong number")

