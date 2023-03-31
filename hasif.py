#inputs
"""x = int(input("Enter a number: "))
if x > 5:
    print("Number is larger than 5")"""

#variables
"""a = "Muhammad"
a = "Hasif" #will override
print(a)"""

#global functions, can use in functions
"""x = "Hasif"
def name():
    print("Muhammad " + x)
name()
print("Who is " + x)"""

#global keywords = once "global" is used, it can be used outside the function, not local anymore. global means it will use the variable outside function unless its not there.
#if its not there, it will automatically make a local variable, global
"""h = "hasif"
def whatisyourname():
    global h
    h = "Hasif"
whatisyourname()
print("My name is " + h)"""

#convert int to complex
"""z = -5
a = complex(z)
print(a)"""

#random, more at w3schools
"""import random
print(random.randrange(1,4))"""

