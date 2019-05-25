import os
import json
from bs4 import BeautifulSoup

allPokemon = []

def get_pokemon_from_file(file, gen):
    pokemon = []

    soup = BeautifulSoup(file, "lxml")

    nameTd = 3
    tableSkip = 1

    # For some reason Serebii changed the format of their attackdex pages but
    # ONLY for gen 3
    if gen == 3:
        tableSkip = 0
        nameTd = 2

    dextables = soup.select(".dextable")

    # Skip the first one because it's just the move description
    for dextable in dextables[tableSkip:]:
        for row in dextable.select("tr")[2:]:
            try:
                name = row.select("td")[nameTd].text
                name = name.replace("Yellow Only", "")
                
                id = row.select("td")[0].text.replace("#", "")

                p = {
                    "name": name,
                    "id": id
                }

                pokemon.append(p)
                allPokemon.append(p)
            except:
                pass

    return pokemon

def get_hm_pokemon_for_gen(gen):
    if gen == 0:
        raise Exception("Gen 0 isn't real!")

    print("Gen {}".format(gen))

    output_dir = "cache/hm_pokemon/gen{}".format(gen)
    input_dir = "cache/raw_html/gen{}".format(gen)

    generation = {}

    for f in os.listdir(input_dir):
        move = os.path.splitext(f)[0]

        pokemon = []

        with open("{}/{}".format(input_dir, f)) as file:
            generation[move] = get_pokemon_from_file(file, gen)

    return generation

if __name__ == '__main__':
    data = {}

    for gen in range(1, 4+1):
        genPokemon = get_hm_pokemon_for_gen(gen)

        data["gen{}".format(gen)] = genPokemon

    with open("cache/all_pokemon.json", "w+") as file:
        file.write(json.dumps(allPokemon, sort_keys=True, indent=4))

    with open("cache/hm_data.json", "w+") as file:
        file.write(json.dumps(data, sort_keys=True, indent=4))
