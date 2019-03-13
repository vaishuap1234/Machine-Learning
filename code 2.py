import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve
from scipy.signal import convolve2d
from scipy import misc
img = misc.ascent()

plt.imshow(img, cmap='gray')

h_kernel = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])
plt.imshow(h_kernel)

s=convolve2d(img, h_kernel)

plt.imshow(s, cmap='gray')
plt.show()