import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

Z = np.exp(-(X**2 + Y**2)) * np.cos(X*3) * np.sin(Y*3)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

surf = ax.contourf(X, Y, Z, levels=50, cmap=cm.viridis)
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_title("Wypełniony wykres konturowy 3D")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
