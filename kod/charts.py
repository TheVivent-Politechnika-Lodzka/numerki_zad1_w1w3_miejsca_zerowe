import numpy as np
import matplotlib.pyplot as plt

def create_chart(func, a, b, points, filename):
    # narysuj linie na 0,0
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # utwórz tablicę, do narysowania wykresu
    x1 = np.arange(a, b, 0.001)
    plt.plot(x1, func(x1))

    # przekształć i narysuj punkty
    points = np.array(points).transpose()
    plt.plot(points[0], points[1], "bo")

    # pokaż
    # plt.show()

    # zapisz
    plt.savefig(filename + ".png")