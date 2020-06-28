import json
import pprint
import cmd
import pyreadline

# TODO this will be unsorted_songs.txt when ready 
f = open("./subset.txt", "r")
library = json.loads(f.read())
f.close()

artists = [song['artist'] for song in library]
artists = list(set(artists))
items = iter(artists)

f = open('sorted_songs.txt', 'r')
playlists = json.loads(f.read())
f.close()


class Command(cmd.Cmd):
    intro = "Hi" 
    prompt = '> '
   
    def complete_sendto(self, text, line, start_index, end_index):
        if text:
            return [
                    playlist for playlist in list(playlists.keys())
                    if playlist.startswith(text)
                ]
        else:
            return list(playlists.keys())
           
    def do_sendto(self, line):
        if line in playlists.keys():
            print("sending "+self.artist+" to playlist "+line)
        else:
            print("playlist does not yet exist.")
            return 
        
        to_pop = []
        artist_songs = []
        for i, song in enumerate(library):
            if (song['artist'] == self.artist):
                artist_songs.append(song)
                to_pop.append(i)
        for i in to_pop:
            library.pop(i)
        
        playlists[line].extend(artist_songs)
    
    def do_info(self, line):
        artist_songs = [song for song in library
                            if song['artist'] == self.artist]
        if (artist_songs):
            for song in artist_songs:
                print('  '+song['title']+', '+str(song['year']))
            print('Genre: '+artist_songs[0]['genre'])

    def do_make(self, line):
        playlists[line] = []

    def do_playlists(self, line):
        for p in playlists:
            print(p)

    def do_next(self, line):
        try:
            self.artist = next(items)
            print(self.artist)
        except StopIteration as e:
            print('all done!')
            return True

    def do_exit(self, line):
        #TODO save_changes()
        #   involves saving playlists as sorted_songs
        #          saving library as unsorted_songs
        return True

    def default(self, line):
        cmd_map = {
            'next': self.do_next, 
            'playlists': self.do_playlists,
            'info': self.do_info,
        }
        for key in cmd_map:
            if key.startswith(line):
                cmd_map[key]('')
                break                
        else:
            print('command does not exist.')


cmd = Command()
cmd.cmdloop()