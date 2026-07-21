# 1 - Create a variable called `first_name` and assign it the value of your first name
first_name = 'AJ'

# 2 - Create a variable called `last_name` and assign it the value of your last name
last_name = 'Wells'

# 3 - Create a third variable called `full_name`, assign it the value of your first and last name
full_name = first_name + ' ' + last_name

# 4 - print the value of `full_name`
print(full_name)

# 5 - Create a variable called `lucky_number` and assign it the value of your lucky number.
lucky_number = 39

# 6 - print this sentence, adding in the variables you created above: 
# 'My name is (full name), and I think (lucky number) is a winner!'.
print(f"My name is {full_name}, and I think {lucky_number} is a winner!")

# 7 - Create a variable named `adventurous` and set it to a boolean value (true or false)
adventurous = True

# 8 - Create a variable named `food`, and set its value to a string of your favorite food
food = 'Italian'

# 9 - Create a variable called `pets` and set it to the value of the number of pets you have
pets = 2

# 10 - Create a variable called `friends_pets` and assign it the value of the number of pets your friend has
friends_pets = 1

# 11 - Add two pets to your `pets` variable
pets += 2

# 12 - Create a constant variable called `allowed_pets` and set it to a number value of your choice
ALLOWED_PETS = 5

# 13 - Create a conditional: if adventurous is true, print "Adventures are great!", 
# otherwise, print "How about we stay home?".
if adventurous:
    print("Adventures are great!")
else:
    print("How about we stay home?")
    
# 14 - Create a compound conditional: if lucky_number is 2 and adventurous is true,
# print "Roll the dice!", otherwise, print "No dice!".
if lucky_number == 2 and adventurous:
    print("Roll the dice!")
    
# 15 - Write a conditional that print "I can have more pets!" 
# if the value of `pets` is less than the value of `allowed_pets`,
# print "I have enough pets" if the value of `pets` is equal to the value of `allowed_pets`,
# and print "Oh no, I have too many pets!"
# if the value of `pets` is greater than the value of `allowed_pets`.

if pets < ALLOWED_PETS:
    print("I can have more pets!")
    
if pets == ALLOWED_PETS:
    print("I have enough pets")
    
if pets > ALLOWED_PETS:
    print("Oh no, I have too many pets!")
    

#  STRETCH GOALS:
#  16 - Make a variable called `most_pets` and a conditional that
#  correctly checks the `pets` and `friends_pets` variables, and
#  assigns the highest value to `most_pets`. There's several possibilities --
#  be sure to think through all the scenarios. 
#  print `most_pets` after the conditional has run.

most_pets = 0
if pets > friends_pets:
    most_pets = pets
    print('I have more pets with ' + str(pets) + '!')
elif pets < friends_pets:
    most_pets = friends_pets
    print('My friend has more pets with ' + str(friends_pets) + '!')
else:
    most_pets = pets
    print('We have the same number of pets with ' + str(pets) + '!')

# 17 - Original lesson asked us to write a switch statement / Python uses match
# It's also written differently 
match (True):
    case True if (pets > friends_pets):
        print('I have more pets with ' + str(pets) + '!')
    case True if (pets < friends_pets):
        print('My friend has more pets with ' + str(friends_pets) + '!')
    case True if (pets == friends_pets):
        print('We have the same number of pets with ' + str(pets) + '!')


# 18 -- Rewrite question 13 with a `ternary` operator. You'll need to do research!
print("Adventures are great!" if adventurous else "How about we stay home?") # Seems more like a if statement, but it is a ternary operator.