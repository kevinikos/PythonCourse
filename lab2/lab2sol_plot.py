from mpl_toolkits.mplot3d import Axes3D
from cs50 import get_int
import matplotlib.pyplot as plt
import numpy as np


print("""#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics "
it's totally up to your imagination how do you want to amend the figure according to the input number (1p)""")

value = get_int("value: ") # suggested range 5-10
limit = 4
start_value = 0
for i in range(0,limit):
	part = value / limit
	print("part:", part)
	start_value += part
	print(start_value)
	x_knots = np.linspace(-start_value, start_value, 200)
	y_knots = np.linspace(-start_value, start_value, 200)
	X, Y = np.meshgrid(x_knots, y_knots)
	R = np.sqrt(X ** 2 + Y ** 2)
	Z = np.sin(R)
	ax = Axes3D(plt.figure(figsize=(8, 5)))
	ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
	plt.show()
