import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = os.getenv("USER_ID")

def get_current_playlists():
    playlists = sp.user_playlists(user_id)

    to_save = []
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            to_save.append({playlist['name']: playlist['uri']})
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    to_save_str = json.dumps(to_save, indent=4)
    f = open("./playlists.txt", "w")
    f.write(to_save_str)
    f.close()

get_current_playlists()
