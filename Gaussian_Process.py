
from __future__ import division
import numpy as np
from kernels import*

default_kernel = Kernel("exponential_kernel", [0.01])


class GP:

	def __init__(self, dataprovider, kernel = default_kernel):
		self.dataprovider = dataprovider
		self.kernel = kernel

	def one_d_prior(self,data_vector):
		N = len(data_vector)
		means = np.zeros(N)
		cov = np.zeros([N,N])
		for i in xrange(N):
			for j in xrange(N):
				cov[i][j] = self.kernel.calculate_kernel_value(data_vector[i], data_vector[j])
		
		#draw from the distribution and return
		return np.random.multivariate_normal(means,cov)


