from matplotlib import pyplot as plt

import sympy as sp
import numpy as np

x = sp.Function('x')
t = sp.symbols('t')

m = 1
k = 1
r = 1
K = 1

dgl = sp.Eq(m*x(t).diff(t,2)+r*x(t).diff(t)+k*x(t), K)

lsg = sp.dsolve(dgl, x(t), ics={x(0): 0, x(1): 0})

print(lsg.rhs)

sp.plot(lsg.rhs,(t,0,10))