#
# -----Multiple Histograms-----
#

import numpy as np
import pylab as pl

primary = [81.8, 92.5, 81.6, 83.8, 81.6,
           95.3, 86.0, 81.2, 85.9, 77.7, 91.1,
           92.9, 86.0, 89.5, 85.0, 86.7, 83.1,
           93.3, 74.4, 89.9, 95.2]

secondary = [78.4, 94.2, 68.3, 79.2, 73.9,
             76.0, 69.0, 66.7, 75.8, 64.8,
             82.6, 60.8, 77.4, 80.0, 79.2,
             94.8, 76.3, 78.7, 83.3, 74.7,
             69.7, 68.8, 86.9, 84.7, 80.4,
             84.9, 73.3]

# Make a single boxplot
pl.boxplot(primary, vert=False)

#Label the x-axis
pl.yticks([1], ["Primary"])
pl.show()