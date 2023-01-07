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

def prediction(pokemon1_num, pokemon2_num, pokedex):
    # we start to get the 2 pokemons info
    pokemon1 = look_info(pokemon1_num, pokedex)
    pokemon2 = look_info(pokemon2_num, pokedex)
    # charging model
    model_prediction = joblib.load('./model/pokemon_model.mod')
    # making a prediction for each pokemon
    pokemon1_prediction = model_prediction.predict([[pokemon1[2], pokemon1[3], pokemon1[4],
                                                    pokemon1[5], pokemon1[6], pokemon1[7], pokemon1[8]]])
    pokemon2_prediction = model_prediction.predict([[pokemon2[2], pokemon2[3], pokemon2[4], pokemon2[5],
                                                     pokemon2[6], pokemon2[7], pokemon2[8]]])
    print('FIGHT: ('+str(pokemon1_num)+')'+pokemon1[1]+' and ('+str(pokemon2_num)+') '+pokemon2[1])
    print('   '+pokemon1[1]+': '+str(pokemon1_prediction[0]))
    print('   '+pokemon2[1]+': '+str(pokemon2_prediction[0]))
    print('')

    if pokemon1_prediction > pokemon2_prediction:
        print(pokemon1[1].upper()+'IS THE WINNER')
    else:
        print(pokemon2[1].upper() + 'IS THE WINNER')

# charge pokedex and throw a battle
with open('./data/pokedex.csv', newline='', encoding='latin_1') as file:
    pokedex = csv.reader(file)
    next(pokedex)
    prediction(368, 598, pokedex)

