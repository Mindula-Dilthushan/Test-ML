import numpy as s
import matplotlib.pyplot as plt

x=s.random.normal(0.0,5.0,1000000)
print(x)

plt.hist(x,100)
plt.show()