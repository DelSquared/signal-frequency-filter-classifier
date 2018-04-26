import numpy as np

N=input("Input how many spectra you would like to generate: ")
s=input("Input starting label: ")

n,m,b,A,f=0,0,0,0,0 #some initialisation

x=np.arange(1000).reshape((1000, 1)) #frequency sweep

def S(x): #define low/high pass curve
    P=(m*x-b)*(-1)**n
    return A/(1+np.exp(P))

for _ in range(int(N)):
    n,m,b,A,f=np.random.uniform(0,1000,5) #b is the cutoff freq
    n=np.floor(n) #determines low/high pass
    f/=1000 #noise level
    A/=10 #frequency difference
    m/=10 #cutoff gradient
    e=np.random.normal(size=(1000,1)) #noise
    y=S(x)+f*e
    np.savetxt('LogRegTest{}.csv'.format(_+int(s)),np.append(x,y,axis=1),fmt='%0.4f', delimiter=',') #save
