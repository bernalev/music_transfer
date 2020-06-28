import json
import pprint
import cmd
import pyreadline

f = open("./songs.txt", "r")
library = json.loads(f.read())
f.close()

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


# loop through library, deleting each item as it gets sorted
#   choose to sort by artist
#       can get more info on songs they own if i don't recognize the artist?
# will it prompt me by artist, or i search by artist?
#   prompt
# autocomplete features just automplete playlist names
# I should also have the option to create a new playlist 
# if i don't finish all in one go, should save intermediate library
f = open('song_stats.txt', 'r')
artists = json.loads(f.read())['artists'].keys()
items = iter(artists)
f.close()

class Command(cmd.Cmd):
    intro = "Hi" 
    prompt = '> '
   
    def do_playlist(self, line):
        # send artist to the playlist
        #artist_songs = [song['title'] for song in library
        #          if song['artist'] ...

        pass

    def do_next(self, line):
        try:
            self.artist = next(items)
            print(self.artist)
        except StopIteration as e:
            print('All done!')
            return True

    def do_exit(self, line):
        return True

    def default(self, line):
        print('ok')


cmd = Command()
cmd.cmdloop()