# Write a function that displays a solid square of a character whose side and the character to be
# printed are specified in integer and character as the function parameters. For example, if side
# is 5 and character is ‘#’, the function should display:
# #####
# #####
# #####
# #####
# #####

def solid_square(n):
    for i in range(n):
        for j in range(1,n+1):
            print('#',end=' ')
        print()
solid_square(5)


