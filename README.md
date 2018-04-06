# signal-frequency-filter-classifier
The application of machine learning techniques (such as logistic regression) to classify a frequency filter from its spectrum

#### Filter classifier from scratch (this time without using SciKitLearn)
As opposed to the previous script (now called ```filterclassifierOLD.py```) this one can easily handle mildly noisy signals like those seen in the testspectra folder. Those signals were constructed by evaluating a logistic function with randomly generated parameters and then perturbed by a low-variance Gaussian noise. The optimisation is done using a gradient descent iterative algorithm (for each coefficient vector *K*,  *K*<sub>*n*+1</sub> = *K*<sub>*n*</sub> - ∇*E* *dt*  where *dt* is the step size or "learning rate" or component-wise  *k*<sub>*n*+1</sub> = *k*<sub>*n*</sub> - *∂<sub>k*</sub>*E* *dt* ) . The mean squared error was used as an error function *E*. The sum was used instead since the factor of <sup>1</sup>/<sub>*n*</sub> is a constant and made irrelevant by the step size. Likewise for the factor of 2 in the partial derivatives so they were also omitted.

The method used can be considered to be a single-input perceptron model *y* = *f*(*wx*+*b*) where *f* is the activation function taken to be a logistic function *f*(*x*) = <sup>1</sup>/<sub>1+exp(-*wx*-*b*)</sub>

#### Further Readings:
- https://en.wikipedia.org/wiki/Gradient_descent
- https://en.wikipedia.org/wiki/Logistic_regression
- https://en.wikipedia.org/wiki/Regression_analysis
- https://en.wikipedia.org/wiki/Logistic_function
- https://en.wikipedia.org/wiki/Mathematical_optimization
