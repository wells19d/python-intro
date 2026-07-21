# EXAMPLE. We make a variable called number and set it to 1 as a number.
# Then increment the number variable so the Number is now 2.
# We check if number is greater than or equal to 2. 2 is equal to 2, so
# we print off if number is greater than or equal to 2. 


# We could just do number = 1, but we want to be explicit that it's a number.
number = int(1)

# In python, we don't have the ++ operator like in javascript, so we have to do it this way.
number += 1

# number += input("Enter a number: ") ## can't do this, it changes it to a string
# print('what happened to number?', number)
# Fires off a unsupported operand type(s) for +=: 'int' and 'str' error

# Let's fix it so that we make sure it's a number.
number += int(input("Enter a number to add: "))

# if we enter 3, we should get back 5
print('what happened to number?', number)

# if we enter 2, we should get back 3
number -= int(input("Enter a number to subtract: "))


# If statements are different in python than javascript, we don't use curly braces, we use indentation to show what is part of the if statement and what is not.
if number >= 2:
    print("Number 2 or more")
else:
    print("Number is less than 2")
    # but how do we end this if statement?
    # python should be smart enough to end it by using another line, 
    # but the indentation is still there, so it thinks it's still part of the statement.
    # So just be sure to remove the indent
    
    
# We make a variable called 'name' and set it to 'Dane'. 
# We check if name should exactly match Mary. We print 'Hello Mary'
# We check if name does not, we print 'Hello <name>'

name = "Dane"

name = input("What is your name? ")
    
if (name == "Mary"):
    print("Hello Mary")
else:
    print("Hello " + name)
        
        
# We make two variables, one called secret with no value, another called code and set the number to 123.
# Create a conditional that if the code matches exactly '123', the value 'secret' turns to 'super'.
# We check if code matches exactly to 123, if so the secret is now super and the code multiplies by 2.
# We check if code is greater than 250, if so the secret is now duper
# Then we print 'secret'

# In javascript we could set this to just secret, but in python we have to set it to an empty string.
secret = ""
code = 123

code = int(input("Enter a code: "))

if (code == 123):
    secret = "super"
    code = code * 2
    
if (code > 250):
    secret = "duper"
    
if (code < 250):
    secret = "Super duper"
    

print('Secret:', secret)

# Make 3 variables ('is_student' and set it to true), (age with a value of 34), (zip with a value of 55407)
# We check 'if' 'is_student' equals exactlys on both sides of the equation, with values true and greater than 80000'. We print `You're a student on the West Coast!`
# We check 'else if' 'is_student' equals exctly, with only one side to be true, with values of false and less than 30. We print `What are your hobbies?`
# We check another 'else if' 'is_student' equals exctly 'true'. We print 'Welcome to Prime!'
# We check with 'else' with no variable (default). We print 'How about the weather?'

# Python, the boolean values are capitalized
is_student = True
age = 34
zip = 55407

if (is_student == True and zip > 80000):
    print("You're a student on the West Coast!")
elif (is_student == False or age < 30):
    print("What are your hobbies?")
    # In python, we don't have an 'else if' statement, we use 'elif' instead.
elif (is_student == True):
    print("Welcome to Prime!")
else:
    print("How about the weather?")
    

# Last part, Javascript uses let and const to declare variables
# In python, we don't have that, we just use the variable name and set it to a value.
# Best practice is to use snake_case for variables and UPPER_SNAKE_CASE for constants, but it's not required, python will still allow the change.