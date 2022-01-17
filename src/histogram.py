import numpy as hg
import matplotlib.pyplot as plt

x=hg.random.uniform(0.5,5.0,100000)
print(x)
plt.hist(x,100)
plt.show()