import numpy as np
from matplotlib import pyplot as plt

#Data, change filename as necessary
Data = np.genfromtxt('testspectra\LogRegTest40.csv', delimiter=',')
#Organising data
X=Data[:,0]
X=np.reshape(X,(X.shape[0],1))
y=Data[:,1]
#Normalising to fit the range [0,1]
Y=(y-np.min(y))/(np.max(y)-np.min(y))


#Smoothing
def Smooth(A,iter):
    K=np.array([7,26,41,26,7])
    K = K/np.sum(K)

    C=A
    for _ in range(A.shape[0]-4):
        C[_+2]=np.sum(A[_:_+5]*K)
        
    #iterative method
    if iter>=1:
        Smooth(C,iter-1) 
    return C

#Iterations
iterations = 20

#Setting up output space
Ynew = np.zeros((iterations+1,Y.shape[0]))

#Setting original data within the output space
Ynew[0] = Y

#Setting different smoothing levels to the output space
for i in range(iterations):
    Ynew[i+1] = Smooth(Ynew[0], i)
    Ynew[0]=Y

#Plotting
plt.plot(X,Ynew[0],label="Data")
plt.ylim(-0.01,1.1)
plt.title("Plotting Various Levels of Smoothing: From 0 to {} iterations".format(iterations))
plt.legend(loc="best")

for _ in range (iterations):
    plt.plot(X, Ynew[_+1], label="{} smoothing iterations".format(_+1))
    plt.ylim(-0.01, 1.1)
    plt.title("Plotting Various Levels of Smoothing: From 0 to {} iterations".format(iterations))
    plt.legend(loc="best")
    
plt.show()
