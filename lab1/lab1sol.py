from matplotlib.pyplot import *
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
	for i in range(1,x):
		fact *= x
		x -= 1
	return fact

print("#2 ask the user for a number and print its factorial (2p)")
# print("factorial:", factorial(x=5),"\n")
print("factorial:", factorial(x=int(input("value: "))),"\n")

#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (2p)

def randomX(limit):
	x = []
	for i in range(0,limit):
		x.append(random.randint(1,99))
	return x

def findMin(x):
	print(x)
	return x.index(min(x)), min(x)

print("#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (2p)")
index, value = findMin(x=randomX(limit=20))
print("index:", index)
print("value:", value, "\n")

#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (2p)

def takeValue(limit):
	x = randomX(limit)
	plotValues = []
	for value in x:
		y = math.exp(value)+2*value
		plotValues.append(y)
	return plotValues

print("""#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (2p)""")
x = takeValue(limit=1000)
print("plot values:")
print(x)
plot(x)
show()











