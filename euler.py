import matplotlib.pyplot as plt
import numpy
import math


h, t0, y0, t_max = 0.001, 0.1, 1, 1
Lt, Ly = [t0], [y0]

def f(t, y):
    return (numpy.tanh(t) - y)/t

def euler(h, t0, y0, t_max):
    t, y = t0, y0

    while t < t_max:
        y = y + h*f(t, y)
        t = t + h
        Ly.append(y)
        Lt.append(t)

    return Lt, Ly



plt.plot(euler(h, t0, y0, t_max))
plt.show()
