def replace(str,char1,char2):
    newStr = ""

    for char in str:
        if char == char1:
            newStr += char2
        else:
            newStr += char
    return newStr

str = 'abcda'
str = replace(str, 'a','e')
print(str)