import os
import json
from bs4 import BeautifulSoup

def get_pokemon_from_file(file):
    pokemon = []

    soup = BeautifulSoup(file, "lxml")

    dextables = soup.select(".dextable")

    # Skip the first one because it's just the move description
    for dextable in dextables[1:]:
        for row in dextable.select("tr")[2:]:
            try:
                name = row.select("td")[3].text
                name = name.replace("Yellow Only", " (Yellow Only)")

                pokemon.append(name)
            except:
                pass

    return pokemon

def get_hm_pokemon_for_gen(gen):
    if gen == 0:
        raise Exception("Gen 0 isn't real!")

    print("Gen {}".format(gen))

    output_dir = "cache/hm_pokemon/gen{}".format(gen)
    input_dir = "cache/raw_html/gen{}".format(gen)

    gen = {}

    for f in os.listdir(input_dir):
        move = os.path.splitext(f)[0]

        pokemon = []

        with open("{}/{}".format(input_dir, f)) as file:
            gen[move] = get_pokemon_from_file(file)

    return gen

if __name__ == '__main__':
    data = {}

    for gen in range(1, 3):
        data["gen{}".format(gen)] = get_hm_pokemon_for_gen(gen)

    with open("cache/hm_data.json", "w+") as file:
        file.write(json.dumps(data, sort_keys=True, indent=4))
