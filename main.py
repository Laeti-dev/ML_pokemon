import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

filesList = os.listdir('./data')
for file in filesList:
    print(file)

# POKEDEX CSV STUDY
pokemons = pd.read_csv('data/pokedex.csv', encoding='latin_1')
# check the df
print(pokemons.head())
# check the columns
print(pokemons.columns.values)
# change LEGENDAIRE feature values to digit
pokemons['LEGENDAIRE'] = (pokemons['LEGENDAIRE'] == 'VRAI').astype(int)
print(pokemons)

# check if missing datas
print(pokemons.shape)
print(pokemons.info())

# find the missing name
print(pokemons[pokemons['NOM'].isnull()])
# find pokemons around him and look in online pokedex
print(pokemons['NOM'][61])
print(pokemons['NOM'][63])
# add the name
# pokemons['NOM'][62] = 'Colossinge'
print(pokemons['NOM'][62])

# -------------------------------------------------------------------------

# COMBATS CSV STUDY
fights = pd.read_csv('data/combats.csv')

# explore df
print(fights.columns.values)
print(fights.head())
print(fights.shape)
print(fights.info())

# JOIN POKEDEX AND COMBATS

# count pokemons fights
hadFirstPosition = fights.groupby(by='Premier_Pokemon').count()
print('first position', hadFirstPosition)

hadSecondPosition = fights.groupby(by='Second_Pokemon').count()
print('second position', hadSecondPosition)

totalFights = hadFirstPosition + hadSecondPosition
totalFights.rename(columns={'Pokemon_Gagnant': 'Fights'}, inplace=True)
print('total fights', totalFights)
print(totalFights)

Victories = fights.groupby(by='Pokemon_Gagnant').count()
print(Victories)

listToAggregate = fights.groupby(by='Pokemon_Gagnant').count()
listToAggregate.sort_index()
print(listToAggregate.columns.values)
listToAggregate.rename(columns={'Premier_Pokemon': 'victories'}, inplace=True)
# add the number of fights
listToAggregate['number_of_fights'] = hadFirstPosition['Second_Pokemon'] + hadSecondPosition['Premier_Pokemon']
# calculate the rate of victory
listToAggregate['victory_Ratio'] = (listToAggregate['victories']/listToAggregate['number_of_fights'])
print(listToAggregate)

# aggregate the two DF
newPokedex = pokemons.merge(listToAggregate, left_on='NUMERO', right_index=True, how='left')
print(newPokedex.info())

# DESCRIPTIVE STATISTICS
print(newPokedex.describe()['POINTS_ATTAQUE'])

# Find most common pokemons
# for type 1
# axe_X = sns.countplot(data= newPokedex, x='TYPE_1', hue='LEGENDAIRE')
# plt.xticks(rotation=90)
# plt.xlabel('Type_1')
# plt.ylabel('Total')
# plt.title('Type_1 Pokemons')
# plt.show()

# for type 2
# axe_X = sns.countplot(data= newPokedex, x='TYPE_2', hue='LEGENDAIRE')
# plt.xticks(rotation=90)
# plt.xlabel('Type_2')
# plt.ylabel('Total')
# plt.title('Type_2 Pokemons')
# plt.show()

# according to their victory
type1VictoryRate = newPokedex.groupby(by='TYPE_1').agg({'victory_Ratio': 'mean'}).sort_values(by='victory_Ratio')
print(type1VictoryRate)

# correlation
corr = newPokedex.loc[:, ['TYPE_1', 'POINTS_DE_VIE', 'POINTS_ATTAQUE',
                          'POINTS_DEFFENCE', 'POINTS_ATTAQUE_SPECIALE',
                         'POINT_DEFENSE_SPECIALE', 'POINTS_VITESSE',
                            'LEGENDAIRE', 'victory_Ratio']].corr()
# sns.heatmap(data=corr,
#             xticklabels=corr.columns,
#             yticklabels=corr.columns,
#             annot=True)
# plt.show()

