import pandas as pd

df = pd.read_csv('./data/combats.csv')
df = pd.DataFrame(df)

test1 = df.query('Premier_Pokemon == 368 & Second_Pokemon == 598')
print(test1)