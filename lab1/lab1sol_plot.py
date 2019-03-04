from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
import random


def drawChart(x1, x2):
	t = np.arange(x1, x2, 0.01)
	s = np.cos(2 * np.pi * t)
	plot(t, s, "y", "*")
	show()


for i in range(0, 5):
	drawChart(x1=0.0, x2=random.uniform(0.5, 10))
