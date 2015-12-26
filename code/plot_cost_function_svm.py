#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

def cost_function(z, v=1):
    if v == 1: 
        y = []
        for i in range(len(z)): 
	    yy = 0 if z[i] <= -1 else (z[i] + 1)
	    y.append(yy)
        return y
    elif v == 0:
        y = []
        for i in range(len(z)): 
	    yy = 0 if z[i] > 1 else (-z[i] + 1)
	    y.append(yy)
        return y


z = np.linspace(-5, 6, 100)  
y1 = cost_function(z, 1) 
y2 = cost_function(z, 0) 
print(y1)

fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True)

axes[0].plot(z, y1)
axes[0].set(title='cost1')
axes[0].set_xlabel(r'$z=\theta^Tx$')
axes[1].plot(z, y2)
axes[1].set(title='cost0')
axes[1].set_ylim(0, 7)
axes[1].set_xlabel(r'$z=\theta^Tx$')

plt.show()
fig.savefig('./cost_function_svm.png')
plt.close()
