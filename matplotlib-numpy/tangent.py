import matplotlib.pyplot as plt # For ploting
import numpy as np # to work with numerical data efficiently

s = 1260*2 # sample rate range
x = np.arange(-s,s) # the points on the x axis for plotting
y = [ np.tan(np.pi*i/180) for i in x]
plt.stem(x,y,'r')
plt.plot(x,y)
plt.savefig("tangent.png", dpi=1080)
plt.show()
