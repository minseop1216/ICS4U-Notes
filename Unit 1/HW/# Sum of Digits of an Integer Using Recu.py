# Sum of Digits of an Integer Using Recursion
#Write a Python program to get the sum of a non-negative integer using recursion.
#Test Data:
#sumDigits(345) -> 12
#sumDigits(45) -> 9

def sumdigit(N):
    if N < 10:
        return N
    else:
        return N % 10 + sumdigit(N//10) 
    
print (sumdigit(67)) 

