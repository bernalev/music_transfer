import json
import pprint

f = open("./songs.txt", "r")
library = json.loads(f.read())
f.close()



# get intel on music to better inform myself on how to make the playlists
def refreshStats():
    stats = {}
    
    stats['num_songs'] = len(library)

    def getCountByKey(key):
        data = {}

        for song in library:
            if key in song:
                if song[key] in data:
                    data[song[key]] += 1
                else:
                    data[song[key]] = 1
            else:
                pprint.pprint(song)

        return dict(sorted(data.items()))

    stats['genres'] = getCountByKey('genre')
    stats['years'] = getCountByKey('year')
    stats['artists'] = getCountByKey('artist')

    f = open('song_stats.txt', 'w')
    f.write(json.dumps(stats, indent=4))
    f.close()

refreshStats()