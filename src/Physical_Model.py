import numpy as np
import matplotlib.pyplot as plt
import math

h = 10
g = 9.81
t = np.arange(0, 1.7, 0.1)
f = h - np.multiply(g, t**2) / 2

fig, ax = plt.subplots(1, 1)
ax.plot(t, f)
plt.title(r'$y = h - \frac{gt^2}{2}$')
ax.set_ylabel('высота, м.')
ax.set_xlabel('время, c.')
ax.grid(True, which='both')
plt.show()
