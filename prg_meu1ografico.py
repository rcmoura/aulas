import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

ax = plt.subplot()
im = ax.imshow(np.arange(100).reshape((10, 10)))


divide = make_axes_locatable(ax)
cax = divide.append_axes("right", size="5%", pad=0.05)

plt.colorbar(im, cax=cax)

plt.show()
