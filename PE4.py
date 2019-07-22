def biggestNumber():
    """finding the biggest palindrome made by the product of two three digit numbers""" 
    number = 0
    acceptedNumber = 0
    palindromes = []
    for i in range(100,1000):
        for j in range(100,1000):
            number = i * j
            acceptedNumber = acceptNumber(number)
            if not acceptedNumber == 0:
                palindromes.append(acceptedNumber)
    return max(palindromes)
            
def acceptNumber(number):
    """checking if the number is a palindrome"""
    accepted = 0
    numberString = str(number)
    if reverse(numberString) == numberString:
        accepted = number 
    return accepted

def reverse(n):
    """reversing the string entered"""
    return n[::-1]
