#Python modules to be imported

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

#dataset loading

boston_dataset = datasets.load_boston()
X_full = boston_dataset.data
Y = boston_dataset.target
print X_full.shape
print Y.shape

# selecting the most discriminative one feature of the SelectKBest class that
# is fitted to the data by using the .fit() method, reducing the dataset
# to a vector with the help of a selection operated by indexing on all the rows and on
# the selected feature, which can be retrieved by the .get_support() method.

selector = SelectKBest(f_regression, k=1)
selector.fit(X_full, Y)
X = X_full[:, selector.get_support()]
print X.shape

# dataset sample shapes
# observations

# plt.scatter(X, Y, color='black')
# plt.show()

# creating a regressor (a simple linear regression with feature
# normalization), training the regressor, and finally plotting the best linear relation (that's
# the linear model of the regressor) between the input and output

# regressor = LinearRegression(normalize=True)
# regressor.fit(X, Y)
# plt.scatter(X, Y, color='black')
# plt.plot(X, regressor.predict(X), color='blue', linewidth=3)
# plt.show()

# using nonlinear models:

# Support Vector Machine (SVM) is a class of models that can easily solve nonlinearities

# regressor = SVR()
# regressor.fit(X, Y)
# plt.scatter(X, Y, color='black')
# plt.scatter(X, regressor.predict(X), color='blue', linewidth=3)
# plt.show()

# Random Forests is another model for the automatic solving of similar problems

regressor = RandomForestRegressor()
regressor.fit(X, Y)
plt.scatter(X, Y, color='black');
plt.scatter(X, regressor.predict(X), color='blue', linewidth=3)
plt.show()