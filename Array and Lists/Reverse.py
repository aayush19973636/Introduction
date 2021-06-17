def reverse_l(li):

    for i in range(len(li)//2):
        li[i], li[-i-1] = li[-i-1], li[i]

li = [1,2,3,5,4]
reverse_l(li)
print(li)