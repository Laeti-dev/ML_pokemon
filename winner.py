import csv
import joblib

# find pokemon info in pokedex from its number and usable by our model
def look_info(number, pokedex):
    pokemon_info = []
    for pokemon in pokedex:
        if int(pokemon[0]) == number:
            pokemon_info.extend([pokemon[0], pokemon[1], pokemon[4], pokemon[5], pokemon[6],
                            pokemon[7], pokemon[8], pokemon[9], pokemon[10]])
            break
    return pokemon_info

def prediction (pokemon1_num, pokemon2_num, pokedex):
    pokemon1 = 
