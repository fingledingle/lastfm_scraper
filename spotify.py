
# 2c6d4e17556345be8a08e0e016de4f06
# 0875d4f8e27c4a088fb8e3e70145091c
#http://localhost:3000.

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotipy with your credentials
client_id = '2c6d4e17556345be8a08e0e016de4f06'
client_secret = '0875d4f8e27c4a088fb8e3e70145091c'
url = 'http://example.com'






scope = 'playlist-modify-public playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri='http://example.com',
                                               show_dialog=True,
                                               scope=scope
                                               )
                    )








def get_most_played_song_uri(artist_name):
    song_list = []
    for artists in artist_name:    
        result = sp.search(q=artists, type='artist')
        if len(result['artists']['items']) > 0:
            artists_id = result['artists']['items'][0]['id']
            top_tracks = sp.artist_top_tracks(artists_id)
            num_tracks_to_return = min(2,len(top_tracks['tracks']))
            print(f'Top {num_tracks_to_return} tracks for {artists}:')
            for track in top_tracks['tracks'][:num_tracks_to_return]:
                print(f'adding the song {track["name"]} by {artists} to playlist')
                song_list.append(track['uri'])
        else:
            print(f'No artist was found with the name "{artists}". ')
    return song_list






user_id = sp.me()['id']

playlist_name = 'Hello my name is jeff'

playlist = sp.user_playlist_create(user_id, playlist_name, public=False)

playlist_id = playlist['id']



artist_name = ['bladee', 'thaiboy', 'ecco2k']
jeff = get_most_played_song_uri(artist_name)





sp.user_playlist_add_tracks(user_id, playlist_id, jeff)











    # artist_id = result['artists']['items'][0]['id']


    # top_tracks = sp.artist_top_tracks(artist_id)


    # most_played_track = top_tracks['tracks'][0]



    # return result['name']



# artist_name = ['bladee', 'thaiboy', 'ecco2k']


# most_played_song = get_most_played_song_uri(artist_name)
# print(f'try to find the artists and it returns{le_empty_list}')


# print(f'the most played song by {artist_name} is {most_played_song}')






# class Spotify:
#     def __init__(self, artist_list client_id, client_secret):


#         self.client_credentials_manager = SpotifyClientCredentials(
#             client_id=client_id, 
#             client_secret=client_secret
#             )
        

#         self.sp = spotipy.Spotify(
#             client_credentials_manager=client_credentials_manager
#             )
        


