def isPalindrome(seq):
    stripped = [char.lower() for char in seq if char.isalpha()]
    return stripped == stripped[::-1]
    
    
print(isPalindrome("nurses run"))