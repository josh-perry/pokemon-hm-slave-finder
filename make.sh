cd scraper

python3 scrape_serebii.py
python3 get_pokemon_from_raw_html.py

cd -

cp scraper/cache/hm_data.json .
