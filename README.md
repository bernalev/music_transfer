I'm switching my music streaming provider from Google Play Music (GPM) to Spotify and although I could move my music over manually or use apps from the Play Store to do so, I thought it would be funner and most satisfying to write scripts to do it.

I'm leveraging the gmusicapi and Spotipy libraries to communicate with GPM and Spotify.

Since GPM and Spotify manage music in a fundamentally different way (library vs playlists), I'm still on the fence about how I'll sort the music and push it over to Spotify. I'll likely sort my library of ~2000 songs by genre and year ranges and plop that into playlists. 

Since I'll want some playlists that don't fit into that pattern (similar genre and year), for example all-time favourites, I might come up with an interactive script to select a song from my GPM library, and to state the playlist that I want it to be copied to; the script should perform autocompletion and be less work than searching for the song on the Spotify app. 
