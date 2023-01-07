import pandas as pd

# STEP 1 = cut observations into training sets (X) and test sets
dataset = pd.read_csv('./data/dataset.csv', delimiter='\t')

print(dataset.shape)
print(dataset.info())

# delete observations without values
dataset = dataset.dropna(axis=0, how='any')
print(dataset.shape)
print(dataset)

# learning set X
X = dataset.iloc[:, 5:12].values
print(X)

# features to predict == victory_ratio y
y = dataset.iloc[:, 16].values
print(y)

# create learning and test sets
from sklearn.model_selection import train_test_split
X_TRAINING, X_VALIDATION, y_TRAINING, y_VALIDATION = train_test_split(X, y, test_size=0.2, random_state=0)
# test_size = 0.2 is to set 20% of our observation for tests
# since we have many predictive variables for one prediction => multiple linear regression

# STEP 2 : learning
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

# algorithm choice:
algorithm = LinearRegression()

# Training thanks to fit function on learning set
algorithm.fit(X_TRAINING, y_TRAINING)

# Prediction on test set (VALIDATION)
predictions = algorithm.predict(X_VALIDATION)

# Evaluate learning precision with r2_score function by conparing predicted (predictions)
# and expected values (y_VALIDATION)
precision = r2_score(y_VALIDATION, predictions)

print('-----------LINEAR REGRESSION--------------')
print('Precision = ' + str(precision))
print('------------------------------------------')

# DECISION TREE
from sklearn.tree import DecisionTreeRegressor
algorithm = DecisionTreeRegressor()

algorithm.fit(X_TRAINING, y_TRAINING)

predictions = algorithm.predict(X_VALIDATION)

precision = r2_score(y_VALIDATION, predictions)

print('-----------DECISION TREE--------------')
print('Precision = ' + str(precision))
print('------------------------------------------')

# RANDOM FOREST
from sklearn.ensemble import RandomForestRegressor
algorithm = RandomForestRegressor()

algorithm.fit(X_TRAINING, y_TRAINING)

predictions = algorithm.predict(X_VALIDATION)

precision = r2_score(y_VALIDATION, predictions)

print('-----------RANDOM FOREST--------------')
print('Precision = ' + str(precision))
print('------------------------------------------')

# save training model
from joblib import dump
file = './model/pokemon_model.mod'
dump(algorithm, file)
