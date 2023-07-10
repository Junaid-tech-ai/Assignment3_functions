# Write a function to find the octal equivalent of the given number. For example: the octal
# equivalent of 50 is 62.
# num=int(input("Enter The Number: \n"))
num=int(input('Enter the Number:\n'))
def decimal_to_octal(num):
    octal_num =" "
    while  num > 0:
        remainder = num % 8
        octal_num = str(remainder) + octal_num
        num //= 8
    return octal_num


octal_number = decimal_to_octal(num)
print(f"The octal equivalent of {num} is {octal_number}")
