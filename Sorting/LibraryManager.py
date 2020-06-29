class LibraryManager:
    def __init__(self, library):
        self.library = library

    def remove_song():
        pass

    def remove_artist():
        pass

    def get_artist_songs():
        pass

    def print_artist_info(self, artist):
        artist_songs = [song for song in self.library
                            if song['artist'] == artist]
        if (artist_songs):
            for song in artist_songs:
                print('  '+song['title']+', '+str(song['year']))
            print('Genre: '+artist_songs[0]['genre'])

    def get_library():
        return self.library