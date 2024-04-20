import requests
while True:
    pokemon_name = input("\nPlease type in the pokemon's name:\t")
    pokemon_name = pokemon_name.lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    req = requests.get(url)
    pokemon_name = pokemon_name.capitalize()

    if req.status_code == 200:
        data = req.json()
        print(f"{pokemon_name} has a height of: {data['height']}cms")
        print('Abilities:\t')
        for ability in  data['abilities']:
            print(f"{pokemon_name} has a {ability['ability']['name'].upper()} ability")

        print('Type of pokemon:\t')
        for type in data['types']:
            print(f"{pokemon_name} is a {type['type']['name'].upper()} type pokemon")
    else:
        print('Please type correct pokemon name')
