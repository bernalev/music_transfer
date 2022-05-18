from typing import List

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


def get_playlist_id_given_name(name: str) -> str:
    playlists = sp.user_playlists(user_id)
    for playlist in playlists['items']:
        if playlist['name'] == name:
            return playlist['id']


def get_playlist_tracks(playlist_id: str) -> List[str]:
    items_raw = sp.playlist_items(playlist_id)
    item_ids = [i['track']['id'] for i in items_raw['items']]

    while items_raw['next']:
        offset = items_raw["offset"]
        limit = items_raw["limit"]
        items_raw = sp.playlist_items(playlist_id, offset=(offset + limit))
        item_ids.extend([i['track']['id'] for i in items_raw['items']])
    return item_ids


def extend_playlist_with_tracks(playlist_id: str, items: List[str]) -> int:
    result = sp.playlist_add_items(playlist_id, items=items)
    return result


if __name__ == '__main__':
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    user_id = os.getenv("USER_ID")

    old_playlist_id = get_playlist_id_given_name('Aged Pop')
    items_to_add = get_playlist_tracks(old_playlist_id)

    new_playlist_id = get_playlist_id_given_name('growing')
    result = extend_playlist_with_tracks(playlist_id=new_playlist_id, items=items_to_add)
    print(f"{result} songs added to {new_playlist_id}")
