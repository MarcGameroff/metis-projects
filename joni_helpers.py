def get_songname(name):
    '''Extracts song's title'''
    if name.text.find('*') > 0:
        released = False
    else:
        released = True
    return name.text.replace("*", "").strip(), released


def get_lyrics(soup):
    '''Extracts song's lyrics'''
    lyrics = soup.find("div", class_="songlyrics").p.text
    if lyrics.find('lyrics unavailable') > 0:
        return ''
    else:
        return lyrics


def get_author(soup):
    '''Extract's author of lyrics'''
    author = soup.find("p", class_="author").text
    if 'by Joni Mitchell' not in author:
        author = 'NOT WRITTEN BY JONI'
    return author


def exclude_songs(name):
    '''List of songs NOT to extract lyris from'''
    exclude_list = ['Big Yellow Taxi 2007', 'Bonderia', 'Like Veils',
                    'The Student Song', 'What Will He Give Me']
    if name in exclude_list:
        return True
    else:
        return False
