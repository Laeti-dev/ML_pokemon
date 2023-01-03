import pandas as pd

dataset = pd.read_csv('./data/dataset.csv', delimiter='\t')

print(dataset.shape)
print(dataset.info())

# delete observations without values
dataset = dataset.dropna(axis=0, how='any')
print(dataset.shape)