import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

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
    playlists = get_saved_playlists()
    if name not in playlists:
        sp.user_playlist_create(user_id, name)
        refresh_saved_playlists()
        playlists = get_saved_playlists()
    playlist_id = playlists[name]

    while len(tracks)>100:
        sp.user_playlist_add_tracks(user_id, playlist_id, tracks[0:100])
        tracks = tracks[100:]
    sp.user_playlist_add_tracks(user_id, playlist_id, tracks)

def get_track_id(artist, song):
    #search_str = 'track:{} artist:{}'.format(song, artist)
    search_str = '{} {}'.format(song, artist)
    result = sp.search(search_str, limit=1)
    if len(result['tracks']['items']):
        return result['tracks']['items'][0]['id']
    else:
        print('{} by {} not found'.format(song, artist))
        return None

def get_sorted_songs():
    file = open('../Sorting/sorted_songs.txt', 'r')
    songs = json.loads(file.read())
    file.close()
    return songs

def save_failed(failed):
    file = open('./failed_songs.txt', 'w')
    file.write(json.dumps(failed, indent=4))
    file.close()

def push_songs():
    sorted_songs = get_sorted_songs()
    
    for playlist in sorted_songs:
        ids = []
        failed = []
        for song in sorted_songs[playlist]:
            id = get_track_id(song['artist'], song['title'])
            if id:
                ids.append(id)
            else:
                failed.append(song)
                
        add_to_playlist(playlist, ids)
        save_failed(failed)



refresh_saved_playlists()
#push_songs()


