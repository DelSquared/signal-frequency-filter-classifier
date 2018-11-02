import numpy as np 
from matplotlib import pyplot as plt
from ConvolutionLib import Convolve

Data = np.genfromtxt('spec.txt', delimiter=',').T[1]
Data = (Data-np.min(Data))/(np.max(Data)-np.min(Data))

kerLow = np.array([5,4,3,2,1,0,-1,-2,-3,-4,-5])
kerMid = np.array([0,1,2,3,4,5,-4,-3,-2,-1,0])
kerHi = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])

kerLo = kerLow/np.max(kerLow)
kerMid = kerMid/np.max(kerMid)
kerHi = kerHi/np.max(kerHi)

convolution = Convolve(Data,kerLo) #This will plot a spike where it finds a "dip" in the frequency spectrum amplitude

plt.plot(Data,label="Data")
plt.plot(convolution,label="Conv")
plt.show()
