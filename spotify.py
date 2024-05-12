
# 2c6d4e17556345be8a08e0e016de4f06
# 0875d4f8e27c4a088fb8e3e70145091c
#http://localhost:3000.

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotipy with your credentials
client_id = '2c6d4e17556345be8a08e0e016de4f06'
client_secret = '0875d4f8e27c4a088fb8e3e70145091c'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

le_empty_list = []

def get_most_played_song_uri(artist_name):

    for artists in artist_name:
        result = sp.search(q=artists, type='artist')
        le_empty_list.append(result)
    return result['artists']['items'][0]['id']


    # artist_id = result['artists']['items'][0]['id']


    # top_tracks = sp.artist_top_tracks(artist_id)


    # most_played_track = top_tracks['tracks'][0]



    # return result['name']



artist_name = ('bladee, thaiboy, ecco2k')


most_played_song = get_most_played_song_uri(artist_name)
print(f'try to find the artists and it returns{most_played_song}')


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
        


