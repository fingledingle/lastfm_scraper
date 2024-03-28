import requests
from bs4 import BeautifulSoup
import random
import time
from scrapingbee import ScrapingBeeClient
PROXY = "WEMYDVA0ROFLSW6HCZ41EW8H3KD5HQW2UM7YV49F55ZSYACY235WESS6RQ3IWOLTBXJNDFEL3FRPDRMN"
class GrabArtist:

    def __init__(self, user_choice):
        self.link_similar = f"https://www.last.fm/music/{user_choice}"
        self.link_artist_genres = f"https://www.last.fm/music/{user_choice}"
        self.client = ScrapingBeeClient(
            api_key=PROXY)


    def get_similar_artists(self):
        page_tries = 0
        artists_list = []
        for page in range(1, 26):
            time.sleep(2)
            print(page)
            other_pages = f"{self.link_similar}/+similar?page={page}"
            response = self.client.get(other_pages)
            response.raise_for_status()
            artist_data = response.text
            soup = BeautifulSoup(artist_data, "html.parser")
            artist = soup.find_all(name="a", class_="link-block-target")
            similar_artist_pages = [artist.getText() for artist in artist]
            print(similar_artist_pages)
            artists_list.append(similar_artist_pages)
            page_tries+=1
        if page_tries != 25:
            print("sowwy i couldnt reach some pwages")
        return artists_list



    def get_genre(self):
        genres = []

        response = self.client.get(self.link_artist_genres)
        artist_data = response.text
        soup = BeautifulSoup(artist_data, "html.parser")


        artist_genres_data = soup.select(selector=".tags-list--global a")
        artist_genres = [artists.getText() for artists in artist_genres_data]
        genres.append(artist_genres)
        return genres


    def get_tag_artists(self, tag):
        self.link_tag = f"https://www.last.fm/tag/{tag}/artists"
        page_tries = 0
        artists_list = []
        for page in range(1, 26):
            time.sleep(2)
            print(page)
            other_pages = f"{self.link_tag}?page={page}"
            response = self.client.get(other_pages)
            response.raise_for_status()
            artist_data = response.text
            soup = BeautifulSoup(artist_data, "html.parser")
            artist = soup.find_all(name="a", class_="link-block-target")
            same_genre_artists = [artist.getText() for artist in artist]
            del same_genre_artists[0:2]
            print(same_genre_artists)
            artists_list.append(same_genre_artists)
            page_tries+=1
        if page_tries != 25:
            print("sowwy i couldnt reach some pwages")
        return artists_list


