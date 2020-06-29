import json
import pprint
import cmd
import pyreadline
import LibraryManager

f = open("./subset.txt", "r")
library = json.loads(f.read())
f.close()
library = LibraryManager.LibraryManager(library)

artists = iter(library.get_artists())

f = open('sorted_songs.txt', 'r')
playlists = json.loads(f.read())
f.close()


class Command(cmd.Cmd):
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

        artist_songs = library.remove_artist(self.artist)

        playlists[line].extend(artist_songs)

    def do_info(self, line):
        library.print_artist(self.artist)

    def do_make(self, line):
        playlists[line] = []

    def do_playlists(self, line):
        for p in playlists:
            print('{}, {} songs'.format(p, len(playlists[p])))

    def do_next(self, line):
        try:
            self.artist = next(artists)
            print(self.artist)
        except StopIteration as e:
            print('all done!')
            return True

    def do_exit(self, line):
        f = open('sorted_songs.txt', 'w')
        f.write(json.dumps(playlists, indent=4))
        f.close()

        f = open('unsorted_songs.txt', 'w')
        f.write(json.dumps(library.get_library(), indent=4))
        f.close()
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