# Topic Modeling the Lyrics of Joni Mitchell

## What is this?

Our fourth project at Metis, Project Fletcher, required that we apply NLP techniques to data of our choice. I decided to do some topic modeling with a corpus that was not very large (i.e., around 200 'documents') but which I suspected was rich enough to yield some distinct topics or themes. The 'documents' were lyrics to each song written and released by my musical idol, Joni Mitchell.

## Files in this directory


* **flask_app/** : This is where the files needed to run the flask app are located. I believe they are complete and can be run locally on your machine by calling ```python flask_app.py``` and then opening 0.0.0.0:8000 in the browser.
* **presentation/** : Contains my presentation material including keynote and ppt slides.
* **prescraped_list.csv** : This is the file I started with. I found it on Reddit and used it to save time on scraping the list of anime on MyAnimeList. Because of this, the list of anime does not go past the end of 2014.
* **get_show_ids.ipynb** : This file takes the prescraped_list.csv and converts it into a more useable format. Results are outputted to ```shows_with_ids.csv```.
* **shows_with_ids.csv** : This is the file outputted by ```get_show_ids.ipynb```.
* **mal_scraping.ipynb** : Scrapes MyAnimeList using the names from ```shows_with_ids.csv``` and merges that file with the new data. Outputs to ```full_anime_data_set.csv```
* **mal_config.txt** : required information to access the MyAnimeList API which is used in ```mal_scraping.ipynb```. No spaces.
* **full_anime_data_set.csv** : main data file containing all information. Used in the flask app.
* **export_titles.ipynb** : Takes the ```full_anime_data_set.csv``` and outputs a list of just the anime titles into the flask app. This is used for the autocomplete feature in the apps search bar.
* **metis_challenge_13.ipynb** : This was where I did some preliminary work while deciding how to procede with the nlp analysis of the anime descriptions.
