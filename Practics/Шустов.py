import sys
import math
import numpy as np
import matplotlib.pylab as plt
import matplotlib.ticker as ticker

a = 0           # lower limit of integration
b = np.pi       # upper limit of integration
c = 0           # x∈[c,d]
d = np.pi       # x∈[c,d]
N = 10          # approximation precision
n = 100         # precision of plot
h = (b-a)/N     # fragmentation step
r = 0.0         # max discrepancy


# integrand function
def f(x, t):
    return np.sin(x + t)*np.cos(x * t)


def trap_dt(arg_x):
    int_sum = 0.5 * (f(arg_x, a) + f(arg_x, b))
    for j in range(1, N):
        int_sum += f(arg_x, a + j * h)
    return int_sum * h


X = np.linspace(c, d, n)

# accurate calculation
Y = (np.cos(X) + np.cos(X)*np.cos(np.pi*X)+np.sin(X)*np.sin(np.pi*X))/(1-X**2)
plt.plot(X, Y)

# approximate calculation
aY = trap_dt(X)
plt.plot(X, aY)

for i in range(n):
    if abs(Y[i] - aY[i]) > r:
        r = abs(Y[i] - aY[i])
print("max discrepancy = ", r)

plt.grid(which='major', color='k')
plt.minorticks_on()
plt.grid(which='minor', color='gray', linestyle=':')
plt.show()
"""
