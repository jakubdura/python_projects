import numpy as np
import matplotlib.pyplot as plt

hours = [6, 9, 12, 15, 21, 24, 27, 30, 36, 39, 45, 48, 57, 60]
happ =  [12, 18, 30, 42, 48, 78, 90, 96, 90, 84, 78, 66, 34, 24]

plt.scatter(hours, happ)
plt.xlabel("Hours")
plt.ylabel("Happiness")
plt.show()

# Model kwadratowy
coeff = np.polyfit(hours, happ, 2)
model = np.poly1d(coeff)

polyline = np.linspace(1, 60, 50)

plt.scatter(hours, happ)
plt.plot(polyline, model(polyline))
plt.show()
