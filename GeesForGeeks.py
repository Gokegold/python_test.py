"""
description: Greeksforgeeks test

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: May 28, 2023

last modification:: [May 28, 2023], [May, 28 2023]

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
# OR
return f"the sum of{numbs_2} and {numbs_1} is {sums}"

      
print(sums)


# question Q
"""
https://pynative.com/python-object-oriented-programming-oop-exercise/

Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
"""
class Vehicle:

    def __init__(self, name, max_speed, mileage, colour="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour


class Bus(Vehicle):
    def bus_details(self):
        return f"Colour: {self.colour}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"


class Car(Vehicle):
    def bus_details(self):
        return f"Colour: {self.colour}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"


buses = Bus("School Volvo", 180, 12)
cars = Car("Audi Q5", 240, 18)

print(Bus.bus_details(buses))
print(Car.bus_details(cars))

"""
https://pynative.com/python-object-oriented-programming-oop-exercise/

OOP Exercise 4: Class Inheritance
Given:

Create a Bus class that inherits from the Vehicle class.
Give the capacity argument of Bus.seating_capacity() a default value of 50.
"""
# question Q1

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    # to print or return the capacity of the child class
    # with the default value of 50
    # we have to call the attribute or the instance in the child class method
    # into the overriden method the will we be able to call the attribute with the 50 capacity.


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())


# Question 6
"""
Given two numbers, write a Python code to find the Maximum of these two numbers.
"""
num_1 = input("Enter a number: ")
num_2 = input("Enter a number: ")

if num_1 >= num_2:
    print(f"{num_1}, is greater and equals to {num_2}")
else:
    print(f"{num_1}, is less than {num_2}")

# OR


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


numbs = maximum(5, 2)
print(numbs)


# OR

def maxi(y, z):
    if y >= z:
        return y
    else:
        return z


print(maxi(2, 4))

# OR


def maxim(a, b):
    if a >= b:
        return a
    else:
        return b


print(maxim(5, 2))

# OR

c = 11
d = 2

max_number = max(c, d)
print(max_number)


# OR using the Ternary Operrator

a = 12
c = 24

print(a if a >= c else C)
      
# OR 
      # python code to find maximum of two numbers

a = 2
b = 4

maxi = lambda a, b: a if a > b else b

print(f'{maxi(a,b)} is a maximum number')


a = 2
b = 4
ot = [a,b]
x.sort()
print(ot[-1])


# using sort()

a = 2
b = 4
c = 6
d = 0
f = 12
e = 7
ot = [a,b, c, d, e, f]
ot.sort()
print(ot[-1])
