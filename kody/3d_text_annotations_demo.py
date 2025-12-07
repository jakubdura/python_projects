from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # rejestruje projekcję 3D

# Tworzenie figury
fig = plt.figure(figsize=(9, 6))

# Tworzenie osi 3D
ax = fig.add_subplot(111, projection='3d')

# --- DEMO 1: Użycie różnych wartości zdir ---
zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
xs = (1, 4, 4, 9, 4, 1)
ys = (2, 5, 8, 10, 1, 2)
zs = (10, 3, 8, 9, 1, 8)

for zdir, x, y, z in zip(zdirs, xs, ys, zs):
    label = f"({x}, {y}, {z}), zdir={zdir}"
    ax.text(x, y, z, label, zdir=zdir)

# --- DEMO 2: Kolor tekstu ---
ax.text(9, 0, 0, "red", color='red')

# --- DEMO 3: Tekst 2D (stała pozycja na ekranie) ---
ax.text2D(0.05, 0.95, "2D Text", transform=ax.transAxes)

#DEMO 3 tekst 2D z kolorem
ax.text2D(0.05, .095, "2D Colored Text", color='darkred', transform=ax.transAxes)

# Ograniczenia i etykiety osi
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

plt.tight_layout()
plt.show()
