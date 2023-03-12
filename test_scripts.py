# Install and Setup

# REPL

# VSCode & Extension



# 1. Variables / Types


# Challenge 1 - Variables

# Python has a bunch of pre-made, built-in tools which you can use to perform tasks. 
# One is these tools is the input() function which allows us to retrieve a user input. 
# You can see these here, including the input() function: https://www.w3schools.com/python/python_ref_functions.asp

# Read about the input() function, try out the example to see how it works, and then only proceed.

# For this challenge, use this input function to ask “What is your favorite color?”. 
# Save the response into a variable named my_input. 
# Then print “Your favorite color is my_input”. 
# So if I type red as my favorite color, it will print “Your favorite color is red”. 

# WORK OUT YOUR SOLUTION HERE
# **********************
# print("Challenge 1 ----------")
# my_input = input("What's your favorite color? ")
# print("You're favorite color is " + my_input)

# 2. Conditional Logic

# Challenge 2 - Conditionals - Rock, Paper, Scissors

# We'll use what we've so far to create the Rock, Paper, Scissors game. Here's how:

# First, you'll need to capture inputs for both Player 1 and Player 2. 

# Next, you'll use conditionals to check the two answers and see who wins. This seems pretty
# complicated on the surface but don't overthink it. Here's some help: 
# If Player 1 plays Paper, then there are only two conditionals to check against (Rock, Scissors).
# This means for each element, there should be two checks, totalling 6 checks overall. Each check 
# should print "Player x wins" with the correct player based on the condition. 

# Finally, there should be a check for the same element being played, i.e. if both players play rock
# then an error message should be printed like "Error, you aren't allowed to play the same thing".

# WORK OUT YOUR SOLUTION HERE
# **********************
# print("Challenge 2. --------")
# p1 = input("Player 1 hand: ").lower()
# p2 = input("Player 2 hand: ").lower()

# if (p1 == p2):
#     print('We have a draw...')
# elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'): 
#     print("Player 1 won HAHA")
# elif (p1 or p2) != ('rock' or 'paper' or 'scissors'):
#     print('some dumb f*ck played the wrong hand')
# else:
#     print('Player 2 wins!!')



# 3. Lists



# Challenge 3 - Lists
# **********************

# Find the solutions using this list

# birds = ["robin", "bluebird", "sparrow", "cardinal"]


# 1. Save "bluebird" in a variable

# WORK OUT YOUR SOLUTION HERE
# bluebird = birds[1]

# 2. Save "cardinal" in a variable

# WORK OUT YOUR SOLUTION HERE
# cardinal = birds[-1]

# 3. Insert "woodpecker" directly behind sparrow in the list

# WORK OUT YOUR SOLUTION HERE
# birds.insert(3, 'woodpecker')

# 4. Reverse the birds list and print it out

# WORK OUT YOUR SOLUTION HERE
# birds.reverse()

# 5. Save the first two birds only into a new variable called two_birds

# WORK OUT YOUR SOLUTION HERE
# two_birds = birds[0:2]

# 6. Print ["sparrow", "cardinal"] using negative indices

# WORK OUT YOUR SOLUTION HERE
# print(birds[-5:-3])




# 4. Loops



# Challenge 4 - Loops

# items = ["steak", "apple", "bread", "butter", "pineapple"]

# 1. Write a 'for loop' that loops through the above list and prints "item is a fruit" or "item is not a fruit" depending on whether it is or not. 
#    Note that it should not say item but the name of the fruit. So 'steak is not a fruit', 'apple is a fruit', etc. 

# WORK OUT YOUR SOLUTION HERE
# **********************
items = ["steak", "apple", "bread", "butter", "pineapple"]

for item in items:
    if item != 'apple' and item != 'pineapple':
        print(item + ' is not a fruit')
    else:
        print(item + ' is a fruit')

# 2. Write a while loop starting with a counter = 1 that multiplies two to your counter, prints the counter, but breaks the loop after the counter reaches 1000. 

# WORK OUT YOUR SOLUTION HERE
# **********************
counter = 1

while counter < 1000:
    counter *= 2
    if counter < 1000:
        print(counter)



# 5. Functions



# Challenge 5 - Functions

# Write a function that takes a list of numbers and prints a new list with only the numbers less than 10 in it.

# WORK OUT YOUR SOLUTION HERE




# 6. Dictionaries

# Challenge 6 - Dictionaries

# college = {
#     "name": "Yale",
#     "founded": "1701",
#     "motto": "Light and truth",
#     "location": "New Haven, Connecticut",
#     "students": 12060
# }

# 1. Loop through dictionary and print all the values (values only)

# WORK OUT YOUR SOLUTION HERE


# 2. Loop through dictionary and print all the keys and values

# WORK OUT YOUR SOLUTION HERE


# 3. Print the "founded" year of the college

# WORK OUT YOUR SOLUTION HERE




# FINAL PROJECT - Password Checker

# 1. Get password input
# 2. Check if password has lowercase, uppercase, a number, and a special character. 
# 3. If the password doesn't meet all four conditions, then reject with the conditions they still need to meet.
# 4. Only accept if all four conditions are met.
# 5. Add a condition to check that password length is greater than 9 digits. If 9 or less, it fails.

# Hints/Suggestions:
# - Break password into list of letters and loop through to check type (upper, lower, etc.). Check out
#   the Python string package for help with upper, lower, and digits. https://docs.python.org/3/library/string.html. Import this package by
#   putting 'import string' at the top of your file. This will import the library and give you access to its methods.
# - Consider creating a function or two to clean up any repetitiveness. 
# - Remember that there are many ways to complete this task. Many programmers will provide many different solutions. Some will
#   be more "efficient" or more "clean" than others. Who cares at this point. Find what solutions works for you AND successfully
#   checks passwords and call it a win!

