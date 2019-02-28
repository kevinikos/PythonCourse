from cs50 import get_int
import math


#0 use alternative way of reading inputs - using library (0.5p)
def task0():
	print("#0 use alternative way of reading inputs - using library (0.5p)")
	x = get_int("x: ")
	y = get_int("y: ")
	print(x, "+", y, "=", x + y, '\n')
	return x, y

#1 perimeter & field of circles with radius X & Y. (1p)
def task1(x, y):
	print("#1 perimeter & field of circles with radius X & Y. (1p)")
	try:
		if x > 0 and y > 0:
			field_X = math.pi * x ** 2
			perimeter_X = 2 * math.pi * x
			field_Y = math.pi * y ** 2
			perimeter_Y = 2 * math.pi * y
			print("X:", x, "Y:", y)
			print("Field X:", round(field_X, 2))
			print("Perimeter X:", round(perimeter_X, 2))
			print("Field Y:", round(field_Y, 2))
			print("Perimeter Y:", round(perimeter_Y, 2), "\n")
		else:
			print("x and y must be greater than 0\n")
	except TypeError:
		print("invalid input data\n")

#2 find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
def task2():
	print("#2 find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)")
	while True:
		x = get_int("x: ")
		y = get_int("y: ")
		print("X:", x, "Y:", y)
		if x % 2 == 0 and y % 2 == 0:
			if x % y == 0:
				print("numbers are even and X is divisible by Y\n")
				break
			else:
				print("numbers are even but X is not divisible by Y")
				print("-" * 10)
		else:
			print("X and/or Y are odd")
			print("-" * 10)

#3 check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
def task3():
	print("#3 check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)")
	x = get_int("x: ")
	y = get_int("y: ")
	print("X:", x, "Y:", y)
	print("X is divisible by Y\n") if x % y == 0 else print("X is not divisible by Y\n")

#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
def task4():
	print("#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google 'python limiting number of decimals'. (1p)")
	x = float(input("x: "))
	y = float(input("y: "))
	print(x, "/", y, "=", round(x / y, 2))
	print("X is divisible by Y") if x % y == 0 else print("X is not divisible by Y")

def main():
	x, y = task0()
	"""for task1 x and y are taken from task0"""
	task1(x,y)
	# task1(x=4, y=3) # example 2
	# task1(x="dog", y=3) # example 3
	task2()
	task3()
	task4()

main()