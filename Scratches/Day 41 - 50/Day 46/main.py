import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy import SpotifyOAuth

year = input("Which year? ")
month = input("Which month? ")
day = input("Which day? ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/")

client_id = "e4a3868bad29481995106425562d5b3b"
client_secret = "3cbda32cc0ff45e390a5cfe17a3e4d3d"

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(song_names)
