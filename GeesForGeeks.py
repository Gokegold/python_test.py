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
