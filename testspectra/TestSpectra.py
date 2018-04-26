import numpy as np

N=input("Input how many spectra you would like to generate: ")
s=input("Input starting label: ")

n,m,b,A,f=0,0,0,0,0 #some initialisation

x=np.linspace(0,20000,80000) #frequency sweep

def S(x): #define low/high pass curve
    P=(m*x-b)*(-1)**n
    return A/(1+np.exp(P))

for _ in range(int(N)):
    n,m,b,A,f=np.random.uniform(0,20000,5) #b is the cutoff freq
    n=np.floor(n) #determines low/high pass
    f/=20000 #noise level
    A/=100 #frequency difference
    m/=100 #cutoff gradient
    e=np.random.normal(size=x.shape) #noise
    y=S(x)+f*e
    y.reshape((x.shape[0],1))
    np.savetxt('LogRegTest{}.csv'.format(_+int(s)),y,fmt='%0.4f', delimiter=',')
