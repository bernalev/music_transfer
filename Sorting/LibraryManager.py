class LibraryManager:
    def __init__(self, library):
        self.library = library

    def remove_song(self, title, artist):
        to_pop = -1
        for i, song in enumerate(self.library):
            if song['title'] == title and song['artist'] == artist:
                to_pop = i
        
        if to_pop >= 0:
            print('Deleting {} by {}'.format(title, artist))
            return self.library.pop(to_pop)
        else:
            print('song not found in library')

    def remove_artist(self, artist):
        to_pop = []
        artist_songs = []

        for i, song in enumerate(self.library):
            if song['artist'] == artist:
                artist_songs.append(song)
                to_pop.append(i)

        to_pop.sort(reverse=True)
        for i in to_pop:
            self.library.pop(i)

        return artist_songs

    def get_artists(self):
        artists = set([song['artist'] for song in self.library])
        return list(artists)

    def get_artist_songs(self, artist):
        return [song for song in self.library
                            if song['artist'] == artist]

    def print_artist(self, artist):
        artist_songs = self.get_artist_songs(artist)

        if artist_songs:
            for song in artist_songs:
                print(song['title'])

    def get_library(self):
        return self.library
