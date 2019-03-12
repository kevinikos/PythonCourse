from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
import random


def drawChart(x2):
	t = np.arange(0.0, x2, 0.01)
	s = np.cos(2 * np.pi * t)
	plot(t, s, "y", "*")
	show()

drawChart(x2=10.0)
