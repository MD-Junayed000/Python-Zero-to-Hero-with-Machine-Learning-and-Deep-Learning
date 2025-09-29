#  training a model like LinearRegression

#You have some 1D input data X and output data y, and you want to fit a linear regression model.

# But LinearRegression expects 2D input for X, not 1D — so we use .reshape(-1, 1)!

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Sample !D input data

X=np.array([1,2,3,4,5]) # is a 1D array of shape (5,)
y=np.array([3,6,9,12,15])

# Reshape X to 2D (because sklearn need 2D for input features)

X=X.reshape(-1,1) #LinearRegression.fit() expects a 2D array of


#Create and train the model

model = LinearRegression()
model.fit(X,y)


# Predict the model
y_pred=model.predict(X)

# Show result
print('Slope (coefficient): ',model.coef_)
print('Intercept: ', model.intercept_)

#Plot

plt.scatter(X,y,color='blue',label='Original Data')
plt.plot(X,y_pred,color='red',label='Regression Line')
plt.legend()

plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.show()



















