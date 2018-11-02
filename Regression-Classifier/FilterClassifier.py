import numpy as np
from matplotlib import pyplot as plt

#Filter classifier from scratch (this time without using SciKitLearn)
#As opposed to the previous script (now called filterclassifierOLD.py) this one can easily handle mildly noisy signals
#like those seen in the testspectra folder. Those signals were constructed by evaluating a logistic function with randomly
#generated parameters and then perturbed by a low-variance Gaussian noise. The optimisation is done using a gradient descent
#iterative algorithm (for each coefficient vector K, K(n+1) = K(n) - Grad(Error)*dt where dt is the step size or "learning
#rate" or component-wise k(n+1) =  k(n) - dError_dk*dt ). The mean squared error was used as an error function. The sum was
#used instead since the factor of 1/n is a constant and made irrelevant by the step size. Likewise for the factor of 2 in the
#partial derivatives so they were also omitted.


w,b=1,1 #coefficients

def Logistic(x,der="none"): #Logistic function, where the string der is used to compactly encode partial derivatives
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

def Error (x,y,der="none"): #Error function, where the string der is used to compactly encode partial derivatives
    if der=="none": 
        return np.sum(np.power((Logistic(x)-y),2)) 
    elif der=="w" or der=="b":
        return np.sum((Logistic(x)-y)*Logistic(x,der))
    else:
        print("Error in function: Error()")

def Train(x,y,epochs=100000,dt=0.1,disp=1000):
    global w,b
    for _ in range(epochs): #epochs is the number of iterations
        if _%disp==0: #display settings
            E=Error(x,y)
            print(E)
            if E<2 or E<1.5: #step-size decrease when at low errors to avoid overshooting
                dt*=0.1
        w,b = w - Error (x,y,"w")*dt, b - Error (x,y,"b")*dt

N=input("import spectrum number: ")

Data = np.genfromtxt('testspectra/LogRegTest{}.csv'.format(N), delimiter=',') #Modify this if different naming convention is used
x=Data[:,0] #data processing and normalisation
X=x/x.shape[0]
y=Data[:,1]
Y=(y-np.min(y))/(np.max(y)-np.min(y))

Train(X,Y) #training

R=Logistic(X) #evaluating predicition curve to compare in a plot

print("\nw:",w," b:",b) #determining high/low-pass from sign of w
if abs(w)==w:
    print("High-pass")
else:
    print("Low-pass")
    
print("Cut-off: ", -b*x.shape[0]/w) #estimating cut-off frequency from b and w

print("Step slope: ", Logistic(-b/w,"x")) #estimating cut-off slope from b, w and the total derivative w.r.t. x

plt.plot(x,Y,label="Data") #plots
plt.plot(x,R,label="Prediction")
plt.legend(loc="best")
plt.show()
