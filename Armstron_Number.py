# Take an integer number as an input from user, write a function that checks weather a given
# number is Armstrong or not. Hint: If sum of the cubes of each digit of the number is equal to
# the number itself, then the number is called an Armstrong number. For example, 153 = (1 * 1
# * 1) + (5 * 5 * 5) + (3 * 3 * 3)

num=int(input("Enter the Number: \n"))
def armstrongNum(num):
    num_str=str(num)
    num_len=len(num_str)
    sum=0
    for digits in num_str:
        sum += int(digits)**num_len
    if sum==num:
        return True
    else:
        return False
print(armstrongNum(num))
