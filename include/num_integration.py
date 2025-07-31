import numpy as np
import matplotlib.pyplot as plt

class NumericalIntegration:
    def __init__ (self,x,y,h):
        self.x = x
        self.y = y
        self.h = h
        self.n = x.shape[0]
    def euler(self):
        y_new = np.zeros(self.n)
        y_new[0] = self.y(self.x[0])
        for i in range(1, self.n):
            y_new[i] = self.y(self.x[i-1]) + self.h*self.y(self.x[i-1])
        return y_new
    def midPoint(self):
        y_new = np.zeros(self.n)
        y_new[0] = self.y(self.x[0])
        for i in range(1,self.n):
            y_new[i] = self.y(self.x[i-1]) + self.h*self.y(self.x[i-1] + self.h/2)
        return y_new
    def rk4(self):
        y_new = np.zeros(self.n)
        y_new[0] = self.y(self.x[0])
        for i in range(1,self.n):
            k1 = self.y(self.x[i-1])
            k2 = self.y(self.x[i-1] + self.h/2)
            k3 = self.y(self.x[i-1] + self.h/2)
            k4 = self.y(self.x[i-1] + self.h)
            y_new[i] = y_new[i-1] + (self.h/6)*(k1 + 2*k2 + 2*k3 + k4)
        return y_new