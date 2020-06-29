class LibraryManager:
    def __init__(self, library):
        self.library = library

    def remove_song(self):
        #TODO
        pass

    def remove_artist(self, artist):
        to_pop = []
        artist_songs = []

        for i, song in enumerate(self.library):
            if song['artist'] == artist:
                artist_songs.append(song)
                to_pop.append(i)

        #TODO is bug
        for i in to_pop:
            self.library.pop(i)

        return artist_songs

    def get_artists(self):
        return [song['artist'] for song in self.library]

    def get_artist_songs(self, artist):
        return [song for song in self.library
                            if song['artist'] == artist]

    def print_artist(self, artist):
        artist_songs = self.get_artist_songs(artist)

        if artist_songs:
            for song in artist_songs:
                print('  '+song['title']+', '+str(song['year']))
            print('Genre: '+artist_songs[0]['genre'])

    def get_library(self):
        return self.library
