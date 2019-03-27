import math


# 1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)
def figure(type, x, y=None):
	try:
		if type == "circle":
			if x > 0:
				print(type, "field:", round(math.pi, 2) * x ** 2)
				return type, round(math.pi, 2) * x ** 2
			else:
				print(type + ":", "x must be greater than 0")

		elif type == "rectangle":
			if x > 0 and y > 0:
				print(type, "field:", x * y)
				return type, x * y
			else:
				print(type + ":", "x and y must be greater than 0")

		elif type == "triangle" or type == "rhombus":
			if x > 0 and y > 0:
				print(type, "field:", x * y / 2)
				return type, x * y / 2
			else:
				print(type + ":", "x and y must be greater than 0")

		else:
			print("no such a figure:", type)

	except TypeError as e:
		print(type + ":", "need both values given")


# 2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
def compare(arg_1=None, arg_2=None):
	"""if first figure does not comply with the conditions then skip next figure"""
	try:
		type1, field1 = figure(*arg_1)
		type2, field2 = figure(*arg_2)
		if field1 > field2:
			print(type1, "has larger field than", type2)
			print("-" * 10)

		elif field1 == field2:
			print("fields of", type1, "and", type2, "are equal to each other")
			print("-" * 10)

		elif field1 < field2:
			print(type2, "has larger field than", type1)
			print("-" * 10)

	except TypeError as e:
		print(e)
		print("can't compare if one of given values is less than 0 (None) or it's another type of figure")
		print("-" * 10)


# 3 Test your solutions (2p)
compare(["triangle", 5, 222], ["rhombus", 3, 2])
compare(["triangle", 5, 2], ["hexagon", 3, 222])
compare(["triangle", -5, 2], ["circle", 3])
compare(["rhombus", 5, 2], ["circle", 331])
compare(["rhombus", 5, 2])