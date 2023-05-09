import matplotlib.pyplot as plt
import numpy as np
import math
from packageDIY.moduleDIY import nrandom
"""
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
"""
"""
arrC = np.array([[1,2],[3,4],[5,6]])
print(arrC.shape)

print(math.trunc(3.9435))
print(math.degrees(math.pi), math.radians(180))
"""
for i in range(5):
    print(nrandom(1, 45, 6))
    print(nrandom(1, 6, 4, True))