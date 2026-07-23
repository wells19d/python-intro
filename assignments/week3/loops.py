# 1. 'for' loop
# Example: a for loop to print numbers from 0 to 3

# Python is different, we don't write
# for (let i=0; i<4; i++) {  
#   console.log(i);
# }
# We use range with an argument

print('Range: 0-3')
for i in range(4):
    print(i)
    
# TODO: Write a for loop to print the numbers from 0 to 5 
print('Range: 0-6')
for i in range(7):
    print(i)
    
# TODO: Write a for loop to print the numbers from 3 to 5
# Specific argument in range, use a second argument
print('Range: 3-5')
for i in range(3,6):
    print(i)
    
# TODO: Write a for loop to print EVEN numbers from 2 to 10
# Use the third argument in range() to increment by 2.
print('Range: 2-10, evens')
for i in range(2,12,2):
    print(i)


# STRETCH: Write a for loop to do a countdown from 5 to 0
# Use a negative step to count backwards.
print('Countdown: 5-0')
for i in range(5, -1, -1):
    print(i)
    
# TODO: Write a for of loop to print each star in the 'stars' array
stars = ['Polaris', 'Gacrux', 'Formalhaut', 'Rigel', 'Deneb']
for star in stars:
    print(star)
    
# STRETCH: enumerate the array of stars
for index, value in enumerate(stars):
    print('Star ' + str(index) + ': ' + value)
    
    