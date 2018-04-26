import numpy as np

N=input("Input how many spectra you would like to generate: ")
s=input("Input starting label: ")

n,m,b,A,f=0,0,0,0,0

x=np.linspace(0,20000,80000)

def S(x):
    P=(m*x+b)*(-1)**n
    return A/(1+np.exp(P))

for _ in range(int(N)):
    n,m,b,A,f=np.random.uniform(0,20000,5)
    n=np.floor(n)
    f/=20000
    A/=100
    m/=100
    e=np.random.normal(size=x.shape)
    y=S(x)+f*e
    y.reshape((x.shape[0],1))
    np.savetxt('LogRegTest{}.csv'.format(_+int(s)),y,fmt='%0.4f', delimiter=',')