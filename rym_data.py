import requests
from bs4 import BeautifulSoup
from scrapingbee import ScrapingBeeClient
import random
import time

PROXY = "PHV7UHVQJVGO8P1Q9V7LFASMWBKHHU87IA6Z39M05NNFL2ANIN68UYMWGDVCOT00HW1Q1OWB8ZGG4PHZ"


class RateYourMusic:
    def __init__(self, user_input):
        self.user_input = user_input
        self.link_single = f"https://rateyourmusic.com/charts/top/single/{user_input}"
        self.link_album = f"https://rateyourmusic.com/charts/top/album/{user_input}"
        self.client = ScrapingBeeClient(
            api_key=PROXY)
        self.user_input = user_input
        


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
    
    def get_playlists(self):
        page_tries = 1
        artists_list = []
        # jeff = True
        # while jeff:
        time.sleep(5)
        print(f'Current page {page_tries}')
        other_pages = f"{self.user_input}/{page_tries}"
        while True:
            try:
                response = self.client.get(other_pages)
                response.raise_for_status()
                website_data = response.text
                soup = BeautifulSoup(website_data, "html.parser")
                # try:
                artists_data = soup.find_all(name='tr', class_=['treven', 'trodd'])
                text_stuff_unorganized = [artist.getText() for artist in artists_data]
                text_organized = []
                for i in text_stuff_unorganized:
                    new_data = i.split('\n')
                    # new_data[0] = new_data[0].split('')
                    new_data[0][0] = new_data[0][0].split('.')
                    print(new_data[0][0])
                    # print(new_data[0])
                print(f'-----------------------{new_data}')
                return False
            except:
                print('erm we ran into an error lets try again buddy')

            
                    
            
            # print(f'---------------------\n{new_data}')
        # print(new_data[0])

        # for characters in new_data[0]:
        #     if characters == '.':
        #         erm = new_data[0].strip(f'{characters}')
        

                    

            
        # for each_tr_tag in soup:
        #     artist_and_songs_data = soup.find(name="tr", class_=['treven', 'trodd'])
        #     print(artist_and_songs_data)



        # for item in artist_and_songs_data:
        # artist_and_stuff = [artist.getText() for artist in artist_and_songs_data]
        # print({artist_and_stuff})





        #     for index, row in enumerate(artist_and_song, start=0):
        #         try:
        #             artist_jeff = {
        #                 index: {
        #                     "artist": artist_and_song[index + index + 1],
        #                     "album": artist_and_song[index + index]
        #                 }
        #             }

        #             artists_list.update(artist_jeff)
        #         except IndexError:
        #             continue

        #     print(artists_list)
        #     page_tries += 1
        # if page_tries != 26:
        #     print("sowwy i couldnt reach some pwages")
        # return artists_list

