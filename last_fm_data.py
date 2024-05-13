import requests
from bs4 import BeautifulSoup
import random
import time
from scrapingbee import ScrapingBeeClient
from spotify import Spotify_thingy



class GrabArtist:


    def __init__(self, user_choice, scrapingbee_key, spotify_key , page_quantity, song_quantity):
        self.link_similar = f"https://www.last.fm/music/{user_choice}"
        self.link_artist_genres = f"https://www.last.fm/music/{user_choice}"
        self.client = ScrapingBeeClient(
            api_key=scrapingbee_key)
        self.page_quantity = int(page_quantity)
        self.user_choice = user_choice
        self.spotify_key = spotify_key
        self.song_quantity = song_quantity
        print(f'We will attempt to access the page {self.link_similar}')
        

    def get_similar_artists(self):
        artists_list = []
        for page in range(1, 26):
            time.sleep(2)   
            other_pages = f"{self.link_similar}/+similar?page={page}"
            response = self.client.get(other_pages)
            response.raise_for_status()
            artist_data = response.text
            soup = BeautifulSoup(artist_data, "html.parser")
            artist = soup.find_all(name="a", class_="link-block-target")
            user_choice_pages = [artist.getText() for artist in artist]
            artists_list.append(user_choice_pages)



            #Check if the quantity matches the quantity that the user chose
            if len(artists_list) == self.page_quantity:
                print('it ended!')
                print('##############################################') 



                if self.page_quantity == 1:
                    print(artists_list)
                    print('lenght was 1')
                    self.method = 'single page'
                    with open(f"user_choices_to_{self.user_choice}", "w", encoding="utf-8") as file:
                        for fellas in artists_list[0]:
                            file.write(f"{fellas}\n")
                    break


                #Flattening if the list is longer than 1 page
                elif self.page_quantity > 1:
                    print(artists_list)
                    print('the lenght was a higher value than 1')
                    self.method = 'multiple pages'
                    long_artist_list = [list_of_names for row in artists_list for list_of_names in row]
                    with open(f"user_choices_to_{self.user_choice}", "w", encoding="utf-8") as file:
                        for fellas in long_artist_list:
                            file.write(f"{fellas}\n")
                    break
                        
            else: 
                print("We're not there yet mate wait a little bit")

        spotify = Spotify_thingy(artists_names=artists_list, song_quantity=self.song_quantity, client_id=self.spotify_key[0], client_secret=self.spotify_key[1], methods=self.method)
        start_searching = spotify.search_and_add()

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


    def get_tag_artists(self):
        self.link_tag = f"https://www.last.fm/tag/{self.user_choice}/artists"
        artists_list = []
        for page in range(1, 26):
            time.sleep(2)
            other_pages = f"{self.link_tag}?page={page}"
            response = self.client.get(other_pages)
            response.raise_for_status()
            artist_data = response.text
            soup = BeautifulSoup(artist_data, "html.parser")
            artist = soup.find_all(name="a", class_="link-block-target")
            same_genre_artists = [artist.getText() for artist in artist]
            del same_genre_artists[0:2]
            artists_list.append(same_genre_artists)



            #Check if the quantity matches the quantity that the user chose
            if len(artists_list) == self.page_quantity:
                print('it ended!')
                print('##############################################')



                if self.page_quantity == 1:
                    print(artists_list)
                    print('lenght was 1')
                    with open(f"user_choices_to_{self.user_choice}", "w", encoding="utf-8") as file:
                        for fellas in artists_list[0]:
                            file.write(f"{fellas}\n")
                    break


                #Flattening if the list is longer than 1 page
                elif self.page_quantity > 1:
                    print(artists_list)
                    print('the lenght was a higher value than 1')
                    long_artist_list = [list_of_names for row in artists_list for list_of_names in row]
                    with open(f"user_choices_to_{self.user_choice}", "w", encoding="utf-8") as file:
                        for fellas in long_artist_list:
                            file.write(f"{fellas}\n")
                    break
                        
            else: 
                print("We're not there yet mate wait a little bit")






        spotify = Spotify_thingy(artists_names=artists_list, song_quantity=self.song_quantity, client_id=self.spotify_key[0], client_secret=self.spotify_key[1])
        start_searching = spotify.search_and_add()
        return artists_list                





