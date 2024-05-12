import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Setup credentials and Spotify client
client_id = '2c6d4e17556345be8a08e0e016de4f06'
client_secret = '0875d4f8e27c4a088fb8e3e70145091c'
redirect_uri = 'http://example.com'
scope = 'playlist-modify-public playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

def get_most_played_song_uri(artist_name):
    song_uris = []  # List to store song URIs
    for artist in artist_name:
        result = sp.search(q=artist, type='artist')
        if result['artists']['items']:
            artist_id = result['artists']['items'][0]['id']
            top_tracks = sp.artist_top_tracks(artist_id)
            for track in top_tracks['tracks'][:2]:  # Get top 2 tracks
                song_uris.append(track['uri'])
                print(f'Adding {track["name"]} by {artist}')
    return song_uris

# Correctly set your playlist_id to a valid Spotify playlist URI


user_id = sp.me()['id']

playlist_name = 'Hello my name is jeff'

playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
    
playlist_id = playlist['id']



artist_names = ['bladee', 'thaiboy', 'ecco2k']
track_uris = get_most_played_song_uri(artist_names)

# Add tracks to playlist and change playlist details
if track_uris:
    sp.playlist_add_items(playlist_id, track_uris)
else:
    print("No tracks to add.")