from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load the environment variables from .env
load_dotenv()

scope = 'user-read-currently-playing'
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
current_track = spotify.current_user_playing_track()
item = current_track['item']
print(f"{item['name']} by {item['artists'][0]['name']}")
