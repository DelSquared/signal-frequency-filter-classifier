# Signal Frequency Filter Classifier
The application of machine learning techniques (such as logistic regression) to classify a frequency filter from its spectrum

#### Content:
- [Intro](https://github.com/DelSquared/signal-frequency-filter-classifier#filter-classifier-from-scratch-this-time-without-using-scikitlearn)
- [Example Output](https://github.com/DelSquared/signal-frequency-filter-classifier#example-output)
- [Further Readings](https://github.com/DelSquared/signal-frequency-filter-classifier#further-readings)

### Filter Classifier From Scratch (this time without using SciKitLearn)
As opposed to the previous script (now called ```filterclassifierOLD.py```) this one can easily handle mildly noisy signals like those seen in the testspectra folder. Those signals were constructed by evaluating a logistic function with randomly generated parameters and then perturbed by a low-variance Gaussian noise. The optimisation is done using a gradient descent iterative algorithm (for each coefficient vector *K*,  *K*<sub>*n*+1</sub> = *K*<sub>*n*</sub> - ∇*E* *dt*  where *dt* is the step size or "learning rate" or component-wise  *k*<sub>*n*+1</sub> = *k*<sub>*n*</sub> - *∂<sub>k*</sub>*E* *dt* ) . The mean squared error was used as an error function *E*. The sum was used instead since the factor of <sup>1</sup>/<sub>*n*</sub> is a constant and made irrelevant by the step size. Likewise for the factor of 2 in the partial derivatives so they were also omitted.

The method used can be considered to be a single-input perceptron model *y* = *f*(*wx*+*b*) where *f* is the activation function taken to be a logistic function *f*(*x*) = <sup>1</sup>/<sub>1+exp(-*wx*-*b*)</sub>. The following image is a good enough visual representation but the *Y* input is excluded

<p align="center">
  <img src="https://www.cs.utexas.edu/~teammco/misc/perceptron/perceptron.png" width="350"/>
</p>
<sub>Image from https://www.cs.utexas.edu/~teammco/misc/perceptron/ </sub>

### Example Output

<p align="center">
  <img src="https://raw.githubusercontent.com/DelSquared/signal-frequency-filter-classifier/master/Example%20Outputs/Example%20Plot.jpeg" width="1000"/>
</p>

```
import spectrum number: 50
412.09381304786876
10.149479221295394
8.410639693560967
7.5498748688980895
7.001944267408166
...
3.4078254544385143
3.401236978917254
3.3947383786798913
3.388327526728673

w: -156.8231823034971  b: 60.583954796858976
Low-pass
Cut-off:  386.70646686847317
Step slope:  -39.205795575874276

Process finished with exit code 0
```
#### Further Readings:
- https://en.wikipedia.org/wiki/Gradient_descent
- https://en.wikipedia.org/wiki/Logistic_regression
- https://en.wikipedia.org/wiki/Regression_analysis
- https://en.wikipedia.org/wiki/Logistic_function
- https://en.wikipedia.org/wiki/Mathematical_optimization
- https://en.wikipedia.org/wiki/Perceptron
