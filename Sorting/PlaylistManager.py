class PlaylistManager:
    def __init__(self, playlists):
        self.playlists = playlists
        self.names = list(playlists.keys())

    def get_names(self):
        return self.names

    def starts_with(self, text):
        if not text:
            return self.names

        return [name for name in self.names
                if name.startswith(text)]

    def add_playlist(self, name):
        if self.has_playlist(name):
            print('playlist already exists')
        else:
            self.playlists[name] = []
            self.names.append(name)

    def has_playlist(self, name):
        if name in self.names:
            return True
        else:
            return False

    def print_playlists(self):
        for p in self.playlists:
            print('{}, {} songs'.format(p, len(self.playlists[p])))

    def get_playlists(self):
        return self.playlists

    def add_to_playlist(self, name, artist, songs):
        if not self.has_playlist(name):
            return

        print("sending "+artist+" to playlist "+name)
        self.playlists[name].extend(songs)