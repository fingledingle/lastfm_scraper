import requests
from bs4 import BeautifulSoup
import random
import time
from scrapingbee import ScrapingBeeClient

class GrabArtist:

    def __init__(self, user_choice):
        get_user_input = user_choice
        self.link = f"https://www.last.fm/music/{get_user_input}"



    def get_similar_artists(self):
        artists_list = []

        first_page = f"{self.link}/+similar"
        proxy_key = "WEMYDVA0ROFLSW6HCZ41EW8H3KD5HQW2UM7YV49F55ZSYACY235WESS6RQ3IWOLTBXJNDFEL3FRPDRMN"

        client = ScrapingBeeClient(
            api_key=proxy_key)

        response = client.get(first_page)


        artist_data = response.text

        soup = BeautifulSoup(artist_data, "html.parser")
        artists_text = soup.find_all(name="a", class_="link-block-target")

        similar_artists = [artist.getText() for artist in artists_text]
        artists_list.append(similar_artists)


        page_tries = 0
        for page in range(1, 26):
            time.sleep(2)
            print(page)
            other_pages = f"{first_page}?page={page}"
            client2 = ScrapingBeeClient(
                api_key=proxy_key)
            response = client2.get(other_pages)
            #Last fm blocks past page 24 even with different user-agent le epic fail
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
            # except:
            #     self.try_proxy()
            #     print("I will try again 1 second ;w;")



    def get_genre_artists(self):
        pass





