from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


print("""#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics "
it's totally up to your imagination how do you want to amend the figure according to the input number (1p)""")
def drawChart(value, frequency):
	# value = get_int("value: ") # suggested range 5-10
	x_knots = np.linspace(-value * np.pi, value * np.pi, frequency)
	y_knots = np.linspace(-value * np.pi, value * np.pi, frequency)
	X, Y = np.meshgrid(x_knots, y_knots)
	R = np.sqrt(X ** 2 + Y ** 2)
	# Z = np.cos(R) ** 2 * np.exp(-0.1 * R)
	Z = np.sin(R)
	ax = Axes3D(plt.figure(figsize=(8, 5)))
	ax.plot_surface(X, Y, Z, cmap='viridis')
	plt.show()

drawChart(value=2, frequency=201)
