# Write a program that simulates coin tossing. For each toss of the coin, the program should
# print Heads or Tails. Let the program toss the coin 100 times, and count the number of times
# each side of the coin appears and then print the results. The program should call a separate
# function flip that takes no arguments and returns 0 for tails and 1 for heads. Note: To get
# random 1 or 0 you can import a random module and then use random.randint(0,1)
import random
def flip_coin():
    return random.randint(0,1)

def coin_toss_simulation(num_tosses):
    heads=0
    tails=0
    for i in range (num_tosses):
        result=flip_coin()
        if result==0:
            print("Heads")
            heads+=1
        else:
            print("Tails")
            tails+=1
    print("heads",heads)
    print("tails",tails)
coin_toss_simulation(100)


