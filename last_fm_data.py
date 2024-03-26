import requests
from bs4 import BeautifulSoup


class GrabArtist:
    def get_artists(self):
        artists_list = []
        artist_name = input("What artist are you looking for?\n")
        response = requests.get(f"https://www.last.fm/music/{artist_name}/+similar")
        response.raise_for_status()
        artist_data = response.text

        soup = BeautifulSoup(artist_data, "html.parser")
        artists_text = soup.find_all(name="a", class_="link-block-target")

        similar_artists = [artist.getText() for artist in artists_text]
        artists_list.append(similar_artists)


        for page in range(2, 24):
            response = requests.get(f"https://www.last.fm/music/{artist_name}/+similar?page={page}")
            #Last fm blocks past page 24 even with different user-agent le epic fail
            response.raise_for_status()
            artist_data = response.text

            soup = BeautifulSoup(artist_data, "html.parser")
            artist = soup.find_all(name="a", class_="link-block-target")
            similar_artist_pages = [artist.getText() for artist in artist]
            artists_list.append(similar_artist_pages)
        return artists_list






