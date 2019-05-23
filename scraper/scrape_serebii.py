import os
import requests
import time

serebii_root = "https://www.serebii.net/"
raw_html_path = "cache/raw_html"

attackdex_paths = [
    "attackdex-rby",
    "attackdex-gs"
]

field_moves = [
    # Gen 1
    ["cut", "surf", "fly", "strength", "flash", "teleport", "dig", "soft-boiled"],
    
    # Gen 2
    ["cut", "fly", "surf", "strength", "flash", "whirlpool", "waterfall", "rock smash", "headbutt", "sweet scent", "milk drink", "teleport", "dig", "softboiled"],
]

def scrape_attackdex(gen):
    if gen == 0:
        raise Exception("Gen 0 isn't real!")

    gen -= 1

    attackdex = serebii_root + attackdex_paths[gen]

    save_directory = "{}/gen{}".format(raw_html_path, gen+1)

    os.makedirs(save_directory, exist_ok=True)

    for _, move in enumerate(field_moves[gen]):
        move = move.replace(" ", "")

        move_url = "{}/{}.shtml".format(attackdex, move)
        save_path = "{}/{}.cshtml".format(save_directory, move)

        if os.path.isfile(save_path):
            print("Skipping {} because we already have it!".format(move_url))
            continue

        print("Fetching {}...".format(move_url))
        r = requests.get(move_url)

        if r.status_code != 200:
            print("{} returned a {}!".format(move_url, r.status_code))
            time.sleep(2)
            continue

        with open(save_path, "w+") as file:
            file.write(r.text)

        print("{} saved".format(save_path))
        time.sleep(2)

def main():
    for g in range(1, 3):
        print("Fetching gen {} field moves".format(g))
        scrape_attackdex(g)
        print("")

if __name__ == '__main__':
    main()
