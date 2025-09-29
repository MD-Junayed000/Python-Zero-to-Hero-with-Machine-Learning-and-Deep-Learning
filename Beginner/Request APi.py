# How to connect to ApI's using Python

import requests

base_url= 'https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}" ### Full URL
    response=requests.get(url)
    print(response)

    if response.status_code==200: ## It is ookkk
        pokemon_data=response.json()
        return pokemon_data
    else:
        print(f'FAiled to retrieved data {response.status_code}')





pokemon_name='pikachu'

pokemon_info=get_pokemon_info(pokemon_name)

if pokemon_info: ### if that exist / true
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")













