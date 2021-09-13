#trouver la limit  en -oo de x/R



from sympy.plotting import plot3d
from sympy import *
import matplotlib.pyplot as plt

x = Symbol("x")
y = Symbol("y")

print(plot3d(x**2+y**2, (x,-5,5), (y,-5,5)))
