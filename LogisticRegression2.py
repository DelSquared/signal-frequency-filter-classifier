import numpy as np
from matplotlib import pyplot as plt

w,b=1,1

def Logistic(x,der="none"):
    L=1/(1+np.exp(-(w*x+b)))
    if der=="none":
        return L
    elif der=="w":
        return L*(1-L)*x
    elif der=="b":
        return L*(1-L)
    elif der=="x":
        return L*(1-L)*w
    else:
        print("Error in function: Logistic()")

def Error (x,y,der="none"):
    if der=="none":
        return np.sum(np.power((Logistic(x)-y),2))
    elif der=="w" or der=="b":
        return np.sum((Logistic(x)-y)*Logistic(x,der))
    else:
        print("Error in function: Error()")

def Train(x,y,epochs=100000,dt=0.1,disp=1000):
    global w,b
    for _ in range(epochs):
        if _%disp==0:
            E=Error(x,y)
            print(E)
            if E<2 or E<1.5:
                dt*=0.1
        w,b = w - Error (x,y,"w")*dt, b - Error (x,y,"b")*dt

N=input("import spectrum number: ")

Data = np.genfromtxt('testspectra/LogRegTest{}.csv'.format(N), delimiter=',')
x=Data[:,0]
X=x/x.shape[0]
y=Data[:,1]
Y=(y-np.min(y))/(np.max(y)-np.min(y))

Train(X,Y)

R=Logistic(X)

print("\nw:",w," b:",b)
if abs(w)==w:
    print("High-pass")
else:
    print("Low-pass")
print("Cut-off: ", -b*x.shape[0]/w)
print("Step slope: ", Logistic(-b/w,"x"))

plt.plot(x,Y,label="Data")
plt.plot(x,R,label="Prediction")
plt.legend(loc="best")
plt.show()
