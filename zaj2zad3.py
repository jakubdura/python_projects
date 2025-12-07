import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)

n_points = 200
x = np.random.normal(loc=0.0, scale=1.0, size=n_points)
y = np.random.normal(loc=0.0, scale=1.0, size=n_points)
z = np.random.normal(loc=0.0, scale=1.0, size=n_points)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(x, y, z, c=z, cmap='viridis', s=30, depthshade=True)

cbar = fig.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Wartość współrzędnej z', rotation=270, labelpad=15)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Wykres 3D – 200 punktów, kolor według z')

ax.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()
