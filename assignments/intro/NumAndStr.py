cups_ver1 = input("Enter the number of cups: ")
price_ver1 = input("Enter the price per cup: ")

total_ver1 = price_ver1 * cups_ver1
print(" Your total is $" + str(total_ver1) + " for " + str(cups_ver1) + " cups.") #This won't work because the variables that are being set as strings.
# one way we could do this is to convert the variable to int or float.

change_cups = int(cups_ver1)
change_price = float(price_ver1)

new_total = change_cups * change_price
print("Your total is $" + str(new_total) + " for " + str(change_cups) + " cups.") # This works because we converted the variables to int and float.
# This method perfectly valid, but now we have more lines of code. We should simplify.

# This is another way we could do this, by converting the variables to int and float in the input function itself. This is a more simplified version of the code above.
cups_ver2 = input("Enter the number of cups: ")
price_ver2 = input("Enter the price per cup: ")
total_ver2 = int(cups_ver2) * float(price_ver2)
print("Your total is $" + str(total_ver2) + " for " + str(cups_ver2) + " cups.") # This is a more simplified version of the code above.

# I think the best way is to:
cups_ver3 = int(input("Enter the number of cups: "))
price_ver3 = float(input("Enter the price per cup: "))
total_ver3 = cups_ver3 * price_ver3
print(f"Your total is ${total_ver3} for {cups_ver3} cups.")