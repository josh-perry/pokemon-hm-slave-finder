# HM Slave Finder
A little project for finding the perfect HM slaves in Pokemon games. This is my first project built using Nuxt so the code is probably garbo.

## What does it do?
### Scraper
The Python scripts in `scraper/` are responsible for scraping serebii.net for all the relevant attackdex pages and parsing the data. They put the data into a nice JSON file called `hm_data.json`. These scripts are most conveniently run by using the `make.sh` file in the root of the project. This script will run all of the python3 files necessary and put the outputs in the right places for the site to run properly.

### Site
The site is a static Nuxt project that uses this data and filters Pokemon depending on which generation and HMs are selected.

Run the site like any other nuxt or vue project: `npm run dev` in the folder.

To generate the site for deployment: run `npm run generate` or `npm run generate:gh-pages` (if you need to deploy it to github-pages, check the package.json and nuxt.config.js to see how that works).

## Screenshot
![Screenshot](/screenshots/1.png?raw=true)

## Link
https://josh-perry.github.io/pokemon-hm-slave-finder/
