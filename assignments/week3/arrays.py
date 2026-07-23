# 1. Creating arrays
# Example: Array of animals
animalArray = ['fish', 'cat', 'bird', 'dog']
print('Animals are:', animalArray)

# TODO: Make an array with some favorite foods & then log it
# to the console with a message similar to the example above
favoriteFoods = ['Steak & Fried Potatoes', 'Chicken Alfredo', 'Chimi Fundidos', 'Wild Bean Tostadas']
print('My favorite foods are:', favoriteFoods)


#  --------------------
# 2. Array.length - tells you how many items are in the array
# Javascript uses .length, Python uses len()

# Example: How many animals are in the array? 
print('We have how many animals?:',len(animalArray))

# TODO: Log to the console the number of foods in your array
print('We have how many favorite foods?: ',len(favoriteFoods))


#  --------------------
# 3. Accessing array items
# Example: Log the first animal from the array using it's array index
print('First Animal:',animalArray[0])

# TODO: Log the second animal in the array 
print('Second Animal:',animalArray[1])

# TODO: Log the last animal in the array using it's array index 
print('4th or Last Animal:',animalArray[3])

# TODO - Stretch: 
# Do this by using the array length instead of the exact index number
print('Last Animal in array:',animalArray[-1])


#  --------------------
# 4. Adding & Removing Array Items
# Example: Add an animal to the end using Array.push
# Javascript uses .push, Python uses .append
animalArray.append('penquin')
print(animalArray[-1], 'was added to the array.')
print('New Animal Array: ',animalArray)

# TODO: Add a new food at the end of your array & log the array
favoriteFoods.append('Lasanga')
print(favoriteFoods[-1], 'was added')
print('New Food Array: ',favoriteFoods)

# Example: Remove the last animal by using Array.pop
removedAnimal = animalArray.pop()
print(removedAnimal,'was removed')
print('New Animal Array:', animalArray)

# TODO: Remove the food at the end of your array & 
#       log both the food removed and the updated array
removedFood = favoriteFoods.pop()
print(removedFood,'was removed')
print('New Food Array:', favoriteFoods)

# Example: Add an animal to the beginning using Array.unshift
# Javascript uses unshift, Python uses insert(), but it also requires an arguement for location.
animalArray.insert(0,'walrus')
print(animalArray[0], 'was added to the animal list')
print('New Animal Array:', animalArray)

# TODO: Add a food at the beginning of the array & log the array
favoriteFoods.insert(0,'Lasanga')
print(favoriteFoods[0], 'was added to the food list')
print('New Food Array:', favoriteFoods)

# Example: Remove the first animal using Array.shift
# Javascript uses shift, Python we again use pop, but with a arguement of position.
removedAnimal = animalArray.pop(0)
print(removedAnimal, 'was removed')
print('New Animal Array:', animalArray)

# TODO: Remove the food at the beginning of your array & 
#       log both the food removed and the updated array

removedFood = favoriteFoods.pop(0)
print(removedFood, 'was removed')
print('New Food Array:', favoriteFoods)