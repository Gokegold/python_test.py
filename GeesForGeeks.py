"""
OOP_test.py

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: May 28, 2023

last modification:: [May 28, 2023]

"""

"""
Given two numbers num1 and num2.
The task is to write a Python program to find the addition of these two numbers. 
"""
# Question 1

def add():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    addition = num1 + num2
    return addition


print(add())

# OR

"""
using static numbers.

num1 = 5
num2 = 3
"""
num_1 = 5
num_2 = 3
sum_num = num_1 + num_2

print(sum_num)
print(f"sum of, {num_1} and {num_2} is {sum_num})

      
# OR
def adding(num1=5, num2=3):
    num3 = num1 + num2
    return f"the addition of {num1} and {num2} is {num3}"


print(adding())

# OR

def adds(num1, num2):
    num3 = num1 + num2
    return f"the addition of {num1} and {num2} is {num3}"


print(adds(5, 3))
      

# Question 3
"""
 Python program to add two numbers using lambda
 
"""
# Driver Code
if __name__ == "__main__":

    number1 = 5
    number2 = 3

    add_num = lambda numbers1, numbers2: number1 + number2

    print(f"the Add_sum is {add_num(number1, number2)}")
    print(f"{number1} and {number2} is {add_num(number1, number2)}")

# Question 4
"""
Defining add function and returning the result.
"""
def plus(a, b):
    return a+b


numb_1 = 10
numb_2 = 5

sum_of_numb = plus(numb_1, numb_2)

print(f"the sum of {numb_1} and {numb_2} is {sum_of_numb}")

# Question 5

"""
Add two numbers in Python using operator.add() method

Initialize two variables num1, and num2.
Find sum using the operator.add() by passing num1, and num2 as arguments and assign to su.
Display num1,num2 and su
"""

import operator

numbs_1 = 15
numbs_2 = 12

sums = operator.add(numbs_1, numbs_2)
print(f"the sums of {numbs_2} and {numbs_1} is {sums}")
