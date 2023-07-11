# Write a function Multiple that considers a pair of integers and determines whether the
# second integer is the multiple of the first or not. The function should take two integers as
# arguments and return True if the second is a multiple of the first, and False otherwise.
num1=int(input("Enter the First Number :"))
num2=int(input("Enter the 2nd Number: "))

def multiple_integers(num1,num2):
    if num1%num2==0:
        return True
    else:
        return False
print( ""multiple_integers(num1,num2))