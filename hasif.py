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

#global keywords = when you want to edit variables that are outside of a function, declare global
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

#format - when you have diff types of variables like num and strings BUT you want to combine
"""name = "Hasif"
age = 19
course = "Infocomm Security"
x = "My name is {}. I am {} years old. I am from {}."
print(x.format(name, age, course))"""

#escape characters = when you try to put "" in a string
"""txt = "Hasif is so called \"too smart\" haha."
print(txt)"""

#insert command
"""about_me = [19, 'lame', 'hardworking']
about_me.insert(2, 'loves to eat')
print(about_me)"""

#slicing = if positive 2:5 means 2-4. If -4:-1 means from the back, -1 to -4, ignore -1
"""b = "Hello, World!"
print(b[-5])"""

#continue, skip that if condition but continue with the rest
"""for i in range(9):
  if i == 3:
    continue
  print(i)"""
