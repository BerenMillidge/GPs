
from __future__ import division
import numpy as np

#This is where we put our kernel functino library
# we're going to slowly try to convert this stuff to julia probably
# or make a julia equalivalent, once it's done
# but for prototyping, it's hard to beat python

class Kernel:
	
	def __init__(self, kernel_type, params):
		self.kernel_type = kernel_type
		self.params = params

	def calculate_kernel_value(self, xi, xj):
		if self.kernel_type=="gaussian":
			return gaussian_kernel(xi, xj, params[0])
		if self.kernel_type=="exponential":
			return exponential_kernel(xi, xj, params[0])



	def polynomial_kernel(x, coefficients, reversed = True):
		length = len(coefficients)
		if reversed:
			total = 0
			for i in xrange(length):
				if i ==0:
					total += coefficients[length]
				else:
					total += coefficients[length-i] * (x ** (coefficients[legnth-i]))
			return total
		if not reversed:
			total = 0;
			for i in xrange(length):
				if i == length:
					total += coefficients[i]
				else:
					total += coefficients[i] * (x**coefficients[i])
			return total;


	def gaussian_kernel(xi, xj, sigma, l):
		return (sigma**2)*np.exp(0.5*((xi-xj)**2)/(l**2))

	def exponential_kernel(xi, xj, l):
		return np.exp((-(xi -xj)**2)/l)

## add more kernels here!
			
		




