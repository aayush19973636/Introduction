import math

def square(x):
    s = int(math.sqrt(x))
    return s*s==x


def checkMember(n):
    return square(5*n*n+4) or square(5*n*n-4)



n = int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
