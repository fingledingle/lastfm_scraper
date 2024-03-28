from last_fm_data import GrabArtist
from test import GetProxy




#I KNOW I COULD PUT THAT ON LASTFMDATA I KNOW THANK YOU FOR NOTICING
def flattening_list(artist_list):
    return [list_of_names for row in artist_list for list_of_names in row]
    # for row in artist_list:
    #   for list_of_names in row   ^^^^^^ basically that



# user_choice = input("What is the artist you're looking for?\n")
# if " " in user_choice:
#     user_choice = user_choice.replace(" ", "+")
#     print(user_choice)


# artist_data = GrabArtist(user_choice)
# similar_artist_list = artist_data.get_similar_artists()
# similar_artists = flattening_list(similar_artist_list)
# print(similar_artists)


proxy_data = GetProxy()
proxy_list = proxy_data.generate_proxy()
