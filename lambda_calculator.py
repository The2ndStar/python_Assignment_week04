#**Assignment 5: Using Lambda Functions in Python**
#Rewrite the functions from Assignment 4 using lambda functions.
#**Instructions:**
#1. Create a new Python file named `lambda_calculator.py`.


#2. Define a lambda function for addition that takes two arguments and returns their sum.
add = lambda x,y : x+y

#3. Define a lambda function for subtraction that takes two arguments and returns their difference.
subtract = lambda x,y : x-y

#4. Define a lambda function for multiplication that takes two arguments and returns their product.
multiply = lambda x,y : x*y

#5. Define a lambda function for division that takes two arguments and returns their quotient.
divide = lambda x,y :x/y

#6. Write a main block that calls each lambda function with sample inputs and prints the results.
x = int(input("X is "))
y = int(input("Y is "))

print("Lambda Calcilator")
print("X + Y = ",add(x, y))
print("X - Y = ",subtract(x, y))
print("X * Y = ",multiply(x, y))
print("X / Y = ",divide(x, y))