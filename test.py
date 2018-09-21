# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import geometry


if __name__ == '__main__':
    origin = geometry.Point3D(500, 500, 0)
    radius = 400
    steps = 8

    circle = geometry.Circle(origin, radius, steps)

    x = []
    y = []

    for p in circle.points:
        x.append(p.x)
        y.append(p.y)

    plt.plot(x, y, 'ro')
    plt.show()
