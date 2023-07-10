# Write a function primeFactor that takes one parameter as its argument and obtain the prime
# factors of the number. Hint: Find all the prime number that multiply together to make the
# original number. e.g. prime factors of 15 are 5 and 3.
factorsList=[]
def primeFactor(x):
    for i in range(1,x+1):
        if x%i==0:
            print(i)
            factorsList.append(i)
    print(factorsList)

x=50

primeFactor(x)