from last_fm_data import GrabArtist
from test import GetProxy




#I KNOW I COULD PUT THAT ON LASTFMDATA I KNOW THANK YOU FOR NOTICING
def flattening_list(artist_list):
    return [list_of_names for row in artist_list for list_of_names in row]
    # for row in artist_list:
    #   for list_of_names in row   ^^^^^^ basically that
    #


user_choice = input("What is the artist you're looking for?\n")
if " " in user_choice:
    user_choice = user_choice.replace(" ", "+")
    print(user_choice)


proxy_data = GetProxy()
proxy_list = proxy_data.generate_proxy()


artist_data = GrabArtist(user_choice)
similar_artist_list = artist_data.get_similar_artists()
similar_artists = flattening_list(similar_artist_list)
with open(f"similar_artists_to_{user_choice}", "w", encoding="utf-8") as file:
    for artist in similar_artists:
        file.write(f"{artist}\n")


print(similar_artists)

