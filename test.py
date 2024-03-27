import requests
from bs4 import BeautifulSoup

def flattening_list(artist_list):
    return [list_of_names for row in artist_list for list_of_names in row]

get_user_input = input("What artist are you looking for?\n")

# link = f"https://www.last.fm/music/{get_user_input}"
#first_page = f"{link}/+similar


artists_list = []
# artist_search = input("What artist are you looking for")
response = requests.get(url=f"https://www.last.fm/music/flica/+similar")
response.raise_for_status()
artist_data = response.text

soup = BeautifulSoup(artist_data, "html.parser")
artists_text = soup.find_all(name="a", class_="link-block-target")

similar_artists = [artist.getText() for artist in artists_text]
artists_list.append(similar_artists)

for page in range(2, 24):
    try:
        other_pages = f"https://www.last.fm/music/{get_user_input}/+similar?page={page}"
        response = requests.get(other_pages)
        # Last fm blocks past page 24 even with different user-agent le epic fail
        response.raise_for_status()
        artist_data = response.text

        soup = BeautifulSoup(artist_data, "html.parser")
        artist = soup.find_all(name="a", class_="link-block-target")
        similar_artist_pages = [artist.getText() for artist in artist]
        artists_list.append(similar_artist_pages)
    except:
        print("sorry brosky didnt work")

similar_artists = flattening_list(artists_list)
print(similar_artists)


