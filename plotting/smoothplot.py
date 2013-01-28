#smoothplot.py
import numpy as np
import pylab as pl

x = np.arange(0, 10, 0.01)
y = x**2

pl.plot(x, y)
pl.show()