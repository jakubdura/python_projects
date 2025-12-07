import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

np.random.seed(123)

def polygon_under_graph(xlist, ylist):
    return [(x, 0) for x in xlist] + list(zip(xlist, ylist))

def main():
    fig, ax = plt.subplots(figsize=(8, 6))

    xs = [np.linspace(0, 10, 50) for i in range(5)]
    ys = [np.random.uniform(0.5, 1.0) * np.sin(xs[i]) for i in range(5)]

    verts = [polygon_under_graph(xs[i], ys[i]) for i in range(5)]
    poly = PolyCollection(verts, alpha=0.6)

    ax.add_collection(poly)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Polygon plot")

    plt.show()

if __name__ == "__main__":
    main()
