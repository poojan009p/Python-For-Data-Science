"""
1) What is a Function?

A function is a block of code that performs a specific task.

Instead of writing the same code repeatedly, you write it once and call it whenever needed.

"""
#-----------------------------------------------------------------------------------------------------------------------------"


def greet(name = "Poojan"):
    print(f"Hello how are you {name}! ")

# greet()


# # function syntax
# def function_name():
#     code


# return statement
def add(a, b):
    return a + b


# Difference between print() and return

def test():
    print(10)

# result = test()  #10

# print(result)   #none

# using return

def test():
    return 10

# result = test()

# print(result)  #10

# Function calling function 

# def square(x):
#     return x * x

# def cube(x):
#     return square(x) * x

# print(cube(9))


# Functions in data science

# missing value 

p = [1,2,3,4,5,6,7,8,9,0,11]

def missing_values(df,column):
    df[column] = df[column].fillna(df[column].mean())
    return df


# Clean column name

def clean_column(df):
    df.columns=(
        df.columns
        .str.lower()
        .str.stripe()
        .str.replace(" ","_")
    )
    return df


# function design practice
# Function Name:
# Input:
# Output:
# Logic:

# Function Name: is_even

# Input: number

# Output:
# True or False

# Logic:
# Check remainder when divided by 2

"-------------------------------------------------------------------"

# Question 1

" Create a function that returns the cube of a number."

def cube(x):
    return x ** 3

# c=cube(2)
# print(c)


# -------------------------------------------------------
# Question 2

# Create a function that returns the larger of two numbers.

def largest_of_two(a,b):
    if a > b:
        return a
    else:
        return b
    
# print(largest_of_two(9,8))

# -------------------------------------------------------

# Question 3

# Create a function that returns the length of a name.

def name_len(name = "Poojan"):
    return len(name)

# print(name_len("poojanThummer"))

# -----------------------------------------------------------

# Question 4

# Create a function that checks whether a person is eligible to vote.

def age(a):
    if a >= 18:
         print("You are eligible to vote")
         
    else :
         print("You are not eligible to vote")
    

# age(18)

# -----------------------------------------------------------

# Question 5

# Create a function that calculates area of rectangle

def area_of_rec(length,width):
    return length*width

# print(area_of_rec(3,3))






