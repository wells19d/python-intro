# print("Hello, World!")
name = input("What is your name?") # This is a prompt, asking the user their name
print("Hello, " + name + "!") # After the user inputs their name, this line runs with the declared variable name.

#slicing
greeting = "Well, Hello there!"
hello = greeting[6:11] # cuts off the string from index 6 to 11, which is "Hello"
print(hello + ", " + name) # This line prints the substring of greeting and the user's name.

age = input("How old are you?") # This is a prompt, asking the user their age
print(age)