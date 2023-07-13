# An integer number is said to be a perfect number if its factors, including 1 (but not the
# number itself), sums up to the number. For example, 6 is a perfect number because 6 = 1 + 2
# + 3. Write a function perfect that determines whether parameter number is a perfect number.
# Use this function in a program that determines and prints all the perfect numbers between 1
# and 1000.

def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum == n

for i in range(1,1001):
    if perfect(i):
        print(i)