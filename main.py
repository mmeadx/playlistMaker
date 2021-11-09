# Imports
import requests
from bs4 import BeautifulSoup as bs
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = 'YOUR ID'
SPOTIFY_SECRET = 'YOUR SECRET'

# Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
print(user_id)

# Asking for Input
billboard_week = input("What week would you like to create a playlist for (YYYY-MM-DD)? ")
who_for = input("Who are you making this for? ")

# Grabbing just the year
billboard_year = billboard_week[:4]

# Scraping Billboards top 100 Chart for a specific date
billboard_endpoint = f'https://www.billboard.com/charts/hot-100/{billboard_week}'
response = requests.get(billboard_endpoint)
billboard_dump = bs(response.text, 'html.parser')

# Putting songs into list and creating txt file
top_100_songs = [song.text for song in billboard_dump.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')]

with open(f'billboard_top_100-{billboard_week}.txt', 'w') as top_100:
    for song in top_100_songs:
        top_100.write(f'{song}\n')

# Create Song URI list
song_uris = []

# Searching for song in Spotify and adding them to URI list
for song in top_100_songs:
    result = sp.search(q=f'track:{song} year:{billboard_year}', type='track')
    print(result)

    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f'{song} does not exist in Spotify, skipped.')

# Creating Playlist in Spotify and adding songs
playlist = sp.user_playlist_create(user=user_id, name=f'{billboard_week} - Billboard Top 100 for {who_for}', public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)