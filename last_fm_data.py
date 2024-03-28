import requests
from bs4 import BeautifulSoup


class GrabArtist:

    def __init__(self, user_choice):
        get_user_input = user_choice
        self.link = f"https://www.last.fm/music/{get_user_input}"



    def ip_adresses(self, proxies):
        
    def get_similar_artists(self):


        first_page = f"{self.link}/+similar"
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }


        artists_list = []
        # artist_search = input("What artist are you looking for")
        response = requests.get(first_page, headers=headers)
        response.raise_for_status()
        artist_data = response.text

        soup = BeautifulSoup(artist_data, "html.parser")
        artists_text = soup.find_all(name="a", class_="link-block-target")

        similar_artists = [artist.getText() for artist in artists_text]
        artists_list.append(similar_artists)



        for page in range(2, 24):
            if page >= 20: #ALSO DOESNT FUCKING WORK FOR NO FUCKING REASON
                continue
            else:
                other_pages = f"{first_page}?page={page}"
                response = requests.get(other_pages, headers=headers)
                #Last fm blocks past page 24 even with different user-agent le epic fail
                response.raise_for_status()
                artist_data = response.text

                soup = BeautifulSoup(artist_data, "html.parser")
                artist = soup.find_all(name="a", class_="link-block-target")
                similar_artist_pages = [artist.getText() for artist in artist]
                artists_list.append(similar_artist_pages)
        return artists_list


    def get_genre_artists(self):
        pass





