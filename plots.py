
#just a library of plotting functions here. nothing too difficult, to make it easy for me

import numpy as np
import matplotlib.pyplot as plt





def plot_one_d_prior(data,vals, show=True):
	
	plt.plot(data, vals, label="example fucntion drawn from GP prior")
	if show:
		plt.show();
	
