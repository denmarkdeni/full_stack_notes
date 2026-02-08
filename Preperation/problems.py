for number in [12,2,34,2,3]:
    print(number)

def isPalindrome(num):
    
    temp = num
    rev = 0
    
    while num > 0 :
        last_digit = num % 10
        rev = (rev * 10) + last_digit
        num = num // 10
    if temp == rev:
        return "palindrome"
    else:
        return "not palindrome"
        
print(isPalindrome(123))
print(isPalindrome(323))