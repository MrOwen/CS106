#smoothplot.py
import numpy as np
import pylab as pl

x = np.arange(0, 2*np.pi , 0.01)
y = np.sin(x)

pl.plot(x, y)
pl.show()