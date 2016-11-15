import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

# Main page with links to all of Joni's songs
url = 'http://jonimitchell.com/music/songlist.cfm'

# Scrape the URLs of lyric pages
response = requests.get(url)
page = response.text
soup = BeautifulSoup(page, "lxml")
song_urls = soup.find_all("a", href=re.compile("^song.cfm"))
print('There are', len(song_urls), 'song links.')

# Preview URLs of first 5 lyric pages
song_urls[:5]

# Store each page-scrape in a list
song_list = []
for song in song_urls:
    songname, released = get_songname(song)
    url = "http://jonimitchell.com/music/" + song['href']
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    lyrics = get_lyrics(soup)
    author = get_author(soup)
    # Create dictionary for a song
    d = {'title': songname,
         'author': author,
         'lyrics': lyrics,
         'released': released}
    if not exclude_songs(songname):
        song_list.append(d)

# Restrict to songs with Joni-penned lyrics
df = pd.DataFrame(song_list)
df2 = df[df.author == 'by Joni Mitchell']
