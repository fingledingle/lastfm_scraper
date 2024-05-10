import requests
from bs4 import BeautifulSoup
import random
import time
from scrapingbee import ScrapingBeeClient




class GrabArtist:


    def __init__(self, similar_artist, scrapingbee_key, page_quantity):
        self.link_similar = f"https://www.last.fm/music/{similar_artist}"
        self.link_artist_genres = f"https://www.last.fm/music/{similar_artist}"
        self.client = ScrapingBeeClient(
            api_key=scrapingbee_key)
        self.page_quantity = int(page_quantity)
        self.similar_artist = similar_artist


    def get_similar_artists(self):
        page_tries = 0
        artists_list = []
        for page in range(1, 26):
            time.sleep(2)
            print(page)
            page_tries+=1     
            other_pages = f"{self.link_similar}/+similar?page={page}"
            response = self.client.get(other_pages)
            response.raise_for_status()
            artist_data = response.text
            soup = BeautifulSoup(artist_data, "html.parser")
            artist = soup.find_all(name="a", class_="link-block-target")
            similar_artist_pages = [artist.getText() for artist in artist]
            print(similar_artist_pages)
            artists_list.append(similar_artist_pages)


            print(f'This is the lenght of the appended artists inside the list {len(artists_list)}')
            print(f'This is the quantity of artists {self.page_quantity}')



            #Check if the quantity matches the quantity that the user chose
            if len(artists_list) == self.page_quantity:
                print('it ended!')
                print('##############################################')



                if self.page_quantity == 1:
                    print(artists_list)
                    print('lenght was 1')
                    with open(f"similar_artists_to_{self.similar_artist}", "w", encoding="utf-8") as file:
                        for fellas in artists_list[0]:
                            file.write(f"{fellas}\n")
                    break


                #Flattening if the list is longer than 1 page
                elif self.page_quantity > 1:
                    print(artists_list)
                    print('the lenght was a higher value than 1')
                    long_artist_list = [list_of_names for row in artists_list for list_of_names in row]
                    with open(f"similar_artists_to_{self.similar_artist}", "w", encoding="utf-8") as file:
                        for fellas in long_artist_list:
                            file.write(f"{fellas}\n")
                    break
                        
            else: 
                print("We're not there yet mate wait a little bit")


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


