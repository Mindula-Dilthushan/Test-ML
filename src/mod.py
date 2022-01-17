from scipy import stats
import numpy as mo
speed=mo.array([5,5,4,2,1,56,67])
x=stats.mode(speed)
print(x)