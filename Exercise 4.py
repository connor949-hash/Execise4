# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple", "banana", "oriange", "date"]
# TODO: Use a for loop to print each fruit in the list
for x in fruits:
    print(x)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown
count = 5
# TODO: Use a while loop to create a countdown from 5 to 1
while count > 0:
    print(count)
    count -=1


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for x in range(1 ,11):
    square = x ** 2
    print(square)
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
Color = ["black","blue","red","purple","gray","cyan"]
# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    print(random.choice(Color))
 
#-------------------------------------------------------------------------

