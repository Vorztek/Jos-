from gen_nombre2 import gen_number
import matplotlib.pyplot as plt

a = gen_number(10,20)
b = gen_number(10,30)

plt.plot(a,b)
plt.show()
