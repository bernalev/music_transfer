from gmusicapi import Mobileclient
import json
import os

api = Mobileclient()
#api.perform_oauth()

device_id = os.getenv("DEVICE_ID")
api.oauth_login(device_id)

library = api.get_all_songs()
library_str = json.dumps(library, indent=4)

f = open("./all_songs.txt", "w")
f.write(library_str)
f.close()