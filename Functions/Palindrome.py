def checkPalindrome(num):
    return str(num) == str(num)[::-1]


num = input()
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
