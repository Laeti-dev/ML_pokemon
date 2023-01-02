import pandas as pd
import os

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
print(pokemons['LEGENDAIRE'])

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

# COMBATS CSV STUDY
fights = pd.read_csv('data/combats.csv')

# explore df
print(fights.columns.values)
print(fights.head())
print(fights.shape)
print(fights.info())

# JOIN POKEDEX AND COMBATS
# count pokemons fights
hadFirstPosition = fights.groupby(by='Premier_Pokemon').count().reset_index()
# hadFirstPosition.columns = ['Pokemon_Number','was_First_position','was_First_Position']
# hadFirstPosition = hadFirstPosition[['Pokemon_Number', 'was_First_Position']]
print(hadFirstPosition)

hadSecondPosition = fights.groupby(by='Second_Pokemon').count().reset_index()
# hadSecondPosition.columns = ['Pokemon_Number','was_Second_position','was_Second_Position']
# hadSecondPosition = hadSecondPosition[['Pokemon_Number','was_Second_position']]
print(hadSecondPosition)

totalFights = hadFirstPosition + hadSecondPosition
totalFights.rename(columns={'Pokemon_Gagnant':'Fights'}, inplace = True)
print(totalFights)
# print(totalFights)

totalOfVictory = fights.groupby(by='Pokemon_Gagnant').count().reset_index()
print(totalOfVictory)

listToAggregate = totalOfVictory[['Pokemon_Gagnant','Premier_Pokemon']]
listToAggregate.rename(columns={'Premier_Pokemon':'victories'}, inplace=True)
# add the number of fights
listToAggregate['number_of_fights'] = hadFirstPosition['Second_Pokemon'] + hadSecondPosition['Premier_Pokemon']
# calculate the rate of victory
listToAggregate['victory_Ratio'] = (listToAggregate['victories']/listToAggregate['number_of_fights'])
print(listToAggregate)

# aggregate the two DF
newPokedex = pokemons.merge(listToAggregate, left_on='NUMERO', right_index=True, how='left')
print(newPokedex.info())

