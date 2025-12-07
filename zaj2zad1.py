import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

# Ustawienie figury (dwukrotnie szersza niż wysoka)
fig = plt.figure(figsize=plt.figaspect(0.5))

# =====================
# Wykres 1: Surface
# =====================
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Tworzenie danych
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Tworzenie powierzchni
surf = ax1.plot_surface(
    X, Y, Z,
    rstride=1,
    cstride=1,
    cmap=cm.coolwarm,
    linewidth=0,
    antialiased=False
)

ax1.set_title("Wykres 3D: Powierzchnia")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")
ax1.set_zlim(-1.01, 1.01)

# Pasek kolorów
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)

# =====================
# Wykres 2: Wireframe
# =====================
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# Te same dane, inna funkcja Z
Z2 = np.cos(R)

# Tworzenie siatki
ax2.plot_wireframe(
    X, Y, Z2,
    rstride=2,
    cstride=2
)

ax2.set_title("Wykres 3D: Siatka")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")

# Pokazanie wykresów
plt.tight_layout()
plt.show()
