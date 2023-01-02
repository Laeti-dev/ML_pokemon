import pandas as pd
import os

filesList = os.listdir('./data')
for file in filesList:
    print(file)


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
