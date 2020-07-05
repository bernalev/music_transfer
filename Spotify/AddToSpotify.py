import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json
import pprint

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = os.getenv("USER_ID")

def refresh_saved_playlists():
    playlists = sp.user_playlists(user_id)
    
    to_save = {}
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            to_save[playlist['name']] = playlist['uri']
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    to_save_str = json.dumps(to_save, indent=4)
    f = open('./playlists.txt', 'w')
    f.write(to_save_str)
    f.close()

def get_saved_playlists():
    f = open('./playlists.txt', 'r')
    playlists = f.read()
    f.close()
    playlists = json.loads(playlists)
    return playlists

def add_to_playlist(name, tracks):
    playlist_id = playlists[name]
    sp.user_playlist_add_tracks(user_id, playlist_id, tracks)

def get_track_id(artist, song):
    search_str = 'track:{} artist:{}'.format(song, artist)
    result = sp.search(search_str, limit=1)
    if len(result['tracks']['items']):
        return result['tracks']['items'][0]['id']
    else:
        print('{} by {} not found'.format(song, artist))
        return None


song_id = get_track_id('eminem', 'mockinggbird')
song_id = get_track_id('eminem', 'mockingbird')

#sp.user_playlist_create(user_id, 'temp')
#refresh_saved_playlists()
playlists = get_saved_playlists()
add_to_playlist('temp', [song_id])


