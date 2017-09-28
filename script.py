import numpy as np
from Gaussian_Process import *
from plots import *

gp = GP(None)
x = np.linspace(-5,5,100)

vals = gp.one_d_prior(x)

plot_one_d_prior(x,vals)


