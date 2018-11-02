import numpy as np 
from matplotlib import pyplot as plt
from ConvolutionLib import Convolve #importing convolution library after compiling with "setup.py" using the batch file

#importing spectrum data and normalisation
Data = np.genfromtxt('spec.txt', delimiter=',').T[1]
Data = (Data-np.min(Data))/(np.max(Data)-np.min(Data))

#defining convolution kernels and normalising them
kerLow = np.array([5,4,3,2,1,0,-1,-2,-3,-4,-5]) #this kernel looks for where the spectrum slopes down
kerMid = np.array([0,1,2,3,4,5,-4,-3,-2,-1,0]) #this kernel HAS NOT YET BEEN TESTED. Intention was to detect triangular spikes.
kerHi = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5]) #this kernel looks for where the spectrum slopes up
kerLo = kerLow/np.max(kerLow)
kerMid = kerMid/np.max(kerMid)
kerHi = kerHi/np.max(kerHi)

#performing convolution
convolution = Convolve(Data,kerLo) #This will plot a spike where it finds a "dip" in the frequency spectrum amplitude

#plot
plt.plot(Data,label="Data")
plt.plot(convolution,label="Conv")
plt.show()
