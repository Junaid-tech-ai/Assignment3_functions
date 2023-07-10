# Write a function named isIn that accepts two strings as arguments and returns True if either
# string occurs anywhere in the other as a substring, and False otherwise. Hint: you might
# want to use the built-in str operation in.

# ----- False Case----------
string1="hello"
string2="python"
def isIn (string1 ,string2):
    return string1 in string2 or string2 in string1

print(isIn(string1,string2))


# -----True Case---------
string1="hello"
string2="hello Python"
def isIn (string1 ,string2):
    return string1 in string2 or string2 in string1

print(isIn(string1,string2))
