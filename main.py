# Do midpoint method and Euler Method on a 2D equation
import numpy as np
from include import num_integration as ni
# import math
import matplotlib.pyplot as plt
h = 1
a = np.arange(0,5, h)
b = lambda x: np.exp(x)
mod = ni.NumericalIntegration(a,b,h)
b_exact = np.exp(a)
b_euler = mod.euler()
b_mid = mod.midPoint()
b_rk4 = mod.rk4()
plt.plot(a,b_exact, label="Exact")
plt.plot(a, b_euler,label="Euler Method")
plt.plot(a, b_mid,label="Mid-Point Method")
plt.plot(a, b_rk4,label="RK4 Method")
plt.legend()
plt.show()