import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression

#Data, change filename as necessary
Data = np.genfromtxt('testspectra\LogRegTest1.csv', delimiter=',')
#Organising data
X=Data[:,0]
X=np.reshape(X,(X.shape[0],1))
y=Data[:,1]
#Normalising to fit the range [0,1]
Y=(y-np.min(y))/(np.max(y)-np.min(y))
Y=np.reshape(Y,(Y.shape[0],1))

#SciKit-Learn's logistic regression to fit a logistic function
logisticRegr = LogisticRegression(max_iter=2000000, tol=0.00000000001)
logisticRegr.fit(X, Y)
#Extracting regression parameters
m,b,a=logisticRegr.coef_,logisticRegr.intercept_,logisticRegr.score(X,Y)
m,b=m[0],b[0]

#Filter classification
if m==abs(m):
    f="High-pass"
else:
    f = "Low-pass"
#Cut-off frequency estimation
cutofffreq=round(abs(b/m)[0])

#Plotting
plt.plot(X,Y,label="Data")
plt.plot(X,logisticRegr.predict(X),label="Prediction")
plt.plot(X,1/(1+np.exp(-2.3025*(m*X+b))),label="Prediction from extracted coeffs.") #This is a known issue where the plot looks less "squished"
plt.title("{} filter with cut off at around: {}Hz".format(f, cutofffreq))
plt.legend(loc="best")
plt.show()
