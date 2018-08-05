#Gaussian Distributions
#With different variances centered around the same average

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu=1
v1 = 1
v2 = v1*2
v3 = v1*4
sigma1 = np.sqrt(v1)
sigma2 = np.sqrt(v1)
sigma3 = np.sqrt(v3)
x=np.arange(15,30,0.05)
x1 = np.linspace(mu-3*sigma1,mu+3*sigma1,100)
x2 = np.linspace(mu-3*sigma2,mu+3*sigma2,100)
x3 = np.linspace(mu-3*sigma3,mu+3*sigma3,100)
p1, = plt.plot(x1,norm.pdf(x1,mu,sigma1),label = 'Plot 1', color='C0')
p2, = plt.plot(x2,norm.pdf(x2,mu,sigma2),label = 'Plot 2', color='C1')
p3, = plt.plot(x3,norm.pdf(x3,mu,sigma3),label = 'Plot 3', color='C2')
plt.legend()
plt.show()

#To get a particular value
a = norm(2,3).pdf(1.5)
print(a) #The value of the variable at x=1.5 in a dsitribution of average 2 and
#Standard deviation of 3 (Variance of 9)
