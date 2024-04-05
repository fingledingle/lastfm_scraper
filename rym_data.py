import requests
from bs4 import BeautifulSoup
from scrapingbee import ScrapingBeeClient
import random
import time

PROXY = "WEMYDVA0ROFLSW6HCZ41EW8H3KD5HQW2UM7YV49F55ZSYACY235WESS6RQ3IWOLTBXJNDFEL3FRPDRMN"


class RateYourMusic:
    def __init__(self, user_input):
        self.link_single = f"https://rateyourmusic.com/charts/top/single/{user_input}"
        self.link_album = f"https://rateyourmusic.com/charts/top/album/{user_input}"
        self.client = ScrapingBeeClient(
            api_key=PROXY)

    def get_top_single(self):
        page_tries = 0
        artists_list = {}
        for page in range(1, 27):
            time.sleep(2)
            print(page)
            other_pages = f"{self.link_single}/{page}"
            response = self.client.get(other_pages)
            response.raise_for_status()
            artist_data = response.text
            soup = BeautifulSoup(artist_data, "html.parser")
            artist_and_songs_data = soup.find_all(name="span", class_="ui_name_locale_original")
            artist_and_song = [artist.getText() for artist in artist_and_songs_data]

            for index, row in enumerate(artist_and_song, start=0):
                try:
                    artist_jeff = {
                        index: {
                            "artist": artist_and_song[index + index + 1],
                            "song": artist_and_song[index + index]
                        }
                    }

                    artists_list.update(artist_jeff)
                except IndexError:
                    continue

            print(artists_list)
            page_tries+=1
        if page_tries != 26:
            print("sowwy i couldnt reach some pwages")
        return artists_list

    def get_top_album(self):
        page_tries = 0
        artists_list = {}
        for page in range(1, 27):
            time.sleep(2)
            print(page)
            other_pages = f"{self.link_single}/{page}"
            response = self.client.get(other_pages)
            response.raise_for_status()
            artist_data = response.text
            soup = BeautifulSoup(artist_data, "html.parser")
            artist_and_songs_data = soup.find_all(name="span", class_="ui_name_locale_original")
            artist_and_song = [artist.getText() for artist in artist_and_songs_data]

            for index, row in enumerate(artist_and_song, start=0):
                try:
                    artist_jeff = {
                        index: {
                            "artist": artist_and_song[index + index + 1],
                            "album": artist_and_song[index + index]
                        }
                    }

                    artists_list.update(artist_jeff)
                except IndexError:
                    continue

            print(artists_list)
            page_tries += 1
        if page_tries != 26:
            print("sowwy i couldnt reach some pwages")
        return artists_list