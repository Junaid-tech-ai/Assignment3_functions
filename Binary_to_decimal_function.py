# Write a function binary2Decimal that take binary number as input and return decimal
# equivalent of the given number.
binary_num=int(input("Enter the binary number: \n"))
def binary_to_decimal(binary_num):
    decimal = 0
    power = 0


    while binary_num > 0:

        remainder = binary_num % 10
        print("remainder =",remainder)


        decimal += remainder * (2 ** power)
        print("decimal =",decimal)


        binary_num //= 10
        power += 1

    return decimal

print(binary_to_decimal(binary_num))
