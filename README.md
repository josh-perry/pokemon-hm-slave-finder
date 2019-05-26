# HM Slave Finder
A little project for finding the perfect HM slaves in Pokemon games. This is my first project built using Nuxt so the code is probably garbo.

## What does it do?
The Python scripts in `scraper/` are responsible for scraping serebii.net for all the relevant attackdex pages and parsing the data. They put the data into a nice JSON file called `hm_data.json` and puts that file into the `site/static/` directory.

The site is a static Nuxt project that uses this data and filters Pokemon depending on which generation and HMs are selected.

## Screenshot
![Screenshot](/screenshots/1.png?raw=true)

## Link
https://josh-perry.github.io/pokemon-hm-slave-finder/
