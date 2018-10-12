import matplotlib.pyplot as plt # For ploting
import numpy as np # to work with numerical data efficiently

s = 360 # sample rate range
x = np.arange(s) # the points on the x axis for plotting
y = [ np.sin(np.pi*i/180) for i in x]
plt.stem(x,y, 'b', 'g')
plt.plot(x,y)
plt.savefig("sine.png", dpi=720)
plt.show()

