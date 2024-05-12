

import spotipy
from spotipy.oauth2 import SpotifyOAuth




class Spotify_thingy:
    def __init__(self, artists_names, song_quantity, client_id, client_secret):
        

        self.artists_names = artists_names
        self.song_quantity = song_quantity
        self.client_id = client_id
        self.client_secret = client_secret



        self.scope = 'playlist-modify-public playlist-modify-private'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                               client_secret=self.client_secret,
                                               redirect_uri='http://example.com',
                                               show_dialog=True,
                                               scope=self.scope
                                               )
                    )
        




        self.user_id = self.sp.me()['id']
        
        self._playlist_name = 'Playlist Made With Jeffbot'
        
        self.playlist = self.sp.user_playlist_create(self.user_id, self._playlist_name, public=False)
        
        self.playlist_id = self.playlist['id']


        self.song_list= []




    def search_and_add(self):

        for artists in self.artists_names:

            result = self.sp.search(q=artists, type='artist')
            #if the quantity of artists items is bigger than 0 then the program runs
            if len(result['artists']['items']) > 0:
                artists_id = result['artists']['items'][0]['id']
                top_tracks = self.sp.artist_top_tracks(artists_id)
                #
                num_tracks_to_return = min(self.song_quantity, len(top_tracks['tracks']))
                print(f'Top {num_tracks_to_return} tracks for {self.artists_names}')
                for track in top_tracks['tracks'][:num_tracks_to_return]:
                    print(f'adding the song {track["name"]} by {artists} to playlist')
                    self.song_list.append(track['uri'])
            else:
                print(f'No artists was found with the name {artists}')
        
        self.sp.user_playlist_add_tracks(self.user_id, self.playlist_id, self.song_list)

        


        


artists_names = ['uami', 'arakoi', 'nuito']

quantity = 3

client_id = '2722e7254a20426488a969a2b94cdfff'
client_secret = '9a65f1340a5441e6a1de69a837043796'


spotify = Spotify_thingy(artists_names=artists_names, song_quantity=quantity, client_id=client_id, client_secret=client_secret)
start_searching = spotify.search_and_add()



