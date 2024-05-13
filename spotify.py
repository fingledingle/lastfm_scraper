
from CTkMessagebox import CTkMessagebox
import spotipy
from spotipy.oauth2 import SpotifyOAuth




class Spotify_thingy:
    def __init__(self, artists_names, song_quantity, client_id, client_secret):
        

        self.artists_names = artists_names
        self.song_quantity = int(song_quantity)
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

        self.song_name_and_artists = {}
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
                print(f'Top {num_tracks_to_return} tracks for {artists}')
                for track in top_tracks['tracks'][:num_tracks_to_return]:
                    print(f'adding the song {track["name"]} by {artists} to playlist')
                    self.song_name_and_artists[f'{artists}'] = {track['name']}
                    self.song_list.append(track['uri'])
            else:
                print(f'No artists was found with the name {artists}')



        msg = CTkMessagebox(title="Hello!", message=f"These songs will be added {self.song_name_and_artists} are you sure you wanna continue?",
                    icon="question", option_1="Yes", option_2="No")
        response = msg.get()

        if response=="Yes":
            self.sp.user_playlist_add_tracks(self.user_id, self.playlist_id, self.song_list)
        else:
            pass

        


    


