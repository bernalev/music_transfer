import json
import pprint
import cmd
import pyreadline
import LibraryManager
import PlaylistManager

class Command(cmd.Cmd):
    prompt = '> '

    def complete_sendto(self, text, line, start_index, end_index):
        return playlists.starts_with(text)

    def do_sendto(self, line):
        if not playlists.has_playlist(line):
            return

        artist_songs = library.remove_artist(self.artist)
        playlists.add_to_playlist(line, self.artist, artist_songs)

    def do_info(self, line):
        library.print_artist(self.artist)

    def do_make(self, line):
        playlists.add_playlist(name=line)

    def do_playlists(self, line):
        playlists.print_playlists()

    def do_next(self, line):
        try:
            self.artist = next(artists)
            print(self.artist)
        except StopIteration as e:
            print('all done!')
            return True

    def do_exit(self, line):
        save_files()
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


def save_files():
    file = open('sorted_songs.txt', 'w')
    file.write(json.dumps(playlists.get_playlists(), indent=4))
    file.close()

    file = open('unsorted_songs.txt', 'w')
    file.write(json.dumps(library.get_library(), indent=4))
    file.close()

def read_files():
    file = open("./unsorted_songs.txt", "r")
    library = json.loads(file.read())
    file.close()

    file = open('sorted_songs.txt', 'r')
    playlists = json.loads(file.read())
    file.close()

    return library, playlists

library, playlists = read_files()
library = LibraryManager.LibraryManager(library)
playlists = PlaylistManager.PlaylistManager(playlists)
artists = iter(library.get_artists())

cmd = Command()
cmd.cmdloop()
