"""
Level 1 → Basic loops
Level 2 → Loops + if statements
Level 3 → Lists and strings
Level 4 → Nested loops
Level 5 → Real-world data problems
Level 6 → NumPy/Pandas operations
"""

"---------------------------------------------------------"

"Level - 1"

# Question 1

# Print numbers from 1 to 10.

# for i in range(1,11):
#     print(i) 

"------------------------------"

# Question 2

# Print numbers from 1 to 20, but only even numbers.

# for i in range(1,21):
#     if i%2 == 0:
#         print(i)

"------------------------------"

# Question 3

# Print numbers from 10 to 1.

# for i in range(11,0,-1):
#     print(i)

"------------------------------"


# Print each fruit from the list.

# fruits = ["Apple", "Banana", "Mango", "Orange"]

# for i in fruits:
#     print(i)


"------------------------------"

# Question 5

# Find the sum of numbers from 1 to 5.

# total = 0
# for i in range(1,6):
#    total += i
# print(f"Total sum = {total}")
             
"----------------------------------------------"

# Question 6

# Count how many items are in the list.

# names = ["John", "Sara", "Mike", "Emma"]

# count = 0

# for i in names:
#    count += 1
# print(count)

"---------------------------------------------"

# Question 7

# Print all characters of a word one by one.

# word = "Python"

# for i in word:
#     print(i)

"---------------------------------------------"

# Question 8

# Print squares of numbers from 1 to 5.

# for i in range(1,6):
#     i = i**2
#     print(i)

"---------------------------------------------"

# Question 9

# Find the largest number in the list.

# numbers = [12, 45, 7, 89, 23]

# largest = numbers[0]

# for i in numbers:
#     if i > largest: 
#         largest = i
# print(largest)
        
"---------------------------------------------"

# Question 10

# Print only numbers greater than 20.

# numbers = [10, 25, 18, 35, 40, 12]

# for i in numbers:
#     if i >= 20:
#      print(i)

"---------------------------------------------"

"""Mini Data Science Practice"""

# Question 11

# Calculate the total sales.

# sales = [100, 200, 150, 300, 250]

# for i in sales:
#     i = sum(sales)
# print(i)

"---------------------------------------------"

# Question 12

# Find the average age.

# ages = [21, 25, 30, 22, 28]

# total = 0
# count = 0

# for i in ages:
#     total += i
#     count += 1
#     average = total/count
# print(average)

"---------------------------------------------"

# Question 13

# Count how many missing values exist.

# data = [10, None, 20, None, 30]

# null_value =0 

# for i in data:
#     if i is None:
#        null_value += 1
# print(null_value)

"---------------------------------------------"

# Question 14

# Print only positive numbers.

# numbers = [-5, 10, -2, 8, 15, -1]

# for i in numbers:
#     if i >= 0: 
#         print(i)
       
"---------------------------------------------"
        
# Question 15

# Find the highest sales value.

sales = [1200, 3400, 2200, 5600, 1800]

highest_value = sales[0]

for i in sales:
     if i > highest_value:
      highest_value = i
print(highest_value)
