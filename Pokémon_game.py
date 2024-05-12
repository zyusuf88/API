# Pokeman game - Pick a pokeman from 1-100 and hope your opponent isn't TALLLER than you ! :)


import requests
import json
import random

def pokemon_generator():
    id = random.randint(1,101)
    return id

player_one = input("Player one : Enter pokemon ID (number 1-100): ")
player_two = input("Player two: Enter pokemon ID (number 1-100): ")


poke_req = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(player_one))
poke_req2 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(player_two))

print(f"{"-" *50}")

poke_data = json.loads(poke_req.text)
poke_data2 = json.loads(poke_req2.text)
# print(type(poke_data))

# two random computer inputs
print(f"Player one : {poke_data['name']}")
print(f"Player two : {poke_data2['name']}")


print(f"{"-" *50}")
def pokemon_compare(player_one, player_two):
    print(f"Player 1's height is : {float(player_one['height']) * 10} cm")
    print(f"Player 2's height is: {float(player_two['height']) * 10} cm")
    if player_one["height"] > player_two["height"]:
        return "Player one has won!"
    elif player_one["height"] == player_two["height"]:
        return "Its a draw!"
    else:
        return "Player two has won!"


print(pokemon_compare(poke_data, poke_data2))