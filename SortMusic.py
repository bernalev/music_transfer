import json
import pprint
import cmd
import pyreadline

f = open("./all_songs.txt", "r")
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

f = open('song_stats.txt', 'r')
artists = json.loads(f.read())['artists'].keys()
items = iter(artists)
f.close()

f = open('sorted_songs.txt', 'r')
playlists = json.loads(f.read())
f.close()

class Command(cmd.Cmd):
    intro = "Hi" 
    prompt = '> '
   
    def complete_playlist(self, text, line, start_index, end_index):
        args = line.split()
        if text:
            return [
                    playlist for playlist in list(playlists.keys())
                    if playlist.startswith(text)
                ]
        else:
            return list(playlists.keys())
           
    def do_playlist(self, line):
        if line in playlists.keys():
            print("sending "+self.artist+" to playlist "+line)
        else:
            print("Playlist does not yet exist.")
            return 
        
        artist_songs = [song for song in library
                            if song['artist'] == self.artist]
        #TODO remove songs from library
        playlists[line].extend(artist_songs)
    
    def do_make(self, line):
        playlists[line] = []

    def do_next(self, line):
        try:
            self.artist = next(items)
            print(self.artist)
        except StopIteration as e:
            print('All done!')
            return True

    def do_exit(self, line):
        #TODO save_changes()
        return True

    def default(self, line):
        print('Command does not exist.')


cmd = Command()
cmd.cmdloop()