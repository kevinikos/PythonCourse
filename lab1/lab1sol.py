from cs50 import get_int
import random
import math

#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (1p)

def fillX():
	x = []
	for i in range(56,101):
		x.append(i)
	return x

def calculateFunc():
	data = fillX()
	func = []
	for x in data:
		y = 2*x**2+2*x+2
		func.append(y)
	return func

print("\n#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (1p)")
print(fillX())
print(calculateFunc(),"\n")

#2 ask the user for a number and print its factorial (2p)

def factorial(x):
	fact = 1
	if x > 0:
		for i in range(1,x):
			fact *= x
			x -= 1
		return fact
	else:
		print("given value must be greater than 0")

print("#2 ask the user for a number and print its factorial (2p)")
# print("factorial:", factorial(x=5),"\n")
print("factorial:", factorial(x=get_int("value: ")),"\n")

#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (2p)

def randomX(limit):
	x = []
	for i in range(0,limit):
		x.append(random.randint(1,99))
	return x

def findMin(x):
	# x = [1,2,3,1,1,1]
	print(x)
	index_list = []
	min_value = min(x)
	min_value_index = x.index(min_value)
	index_list.append(min_value_index)
	for i in range(0,len(x)):
		if (min_value == x[i]) and (min_value_index != i):
			index_list.append(i)
	return index_list, min_value

print("#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (2p)")
index, value = findMin(x=randomX(limit=20))
print("index:", index)
print("value:", value)