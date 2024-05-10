
import rym_data

from rym_data import RateYourMusic
from ui import MainWindow, StartPage
from customtkinter import *
from PIL import Image

from CTkMessagebox import CTkMessagebox


# def flattening_list(artist_list):
#     return [list_of_names for row in artist_list for list_of_names in row]

# def by_similar_lastfm(user_input):


#     grab_artists = GrabArtist(user_input)
#     artist_list = grab_artists.get_similar_artists()



#     similar_artists = flattening_list(artist_list)




    # artist_tags = grab_artists.get_genre()

    # with open(f"similar_artists_to_{user_input}", "w", encoding="utf-8") as file:
    #     for artist in similar_artists:
    #         file.write(f"{artist}\n")













#I KNOW I COULD PUT THAT ON LASTFMDATA I KNOW THANK YOU FOR NOTICING
# def flattening_list(artist_list):
#     return [list_of_names for row in artist_list for list_of_names in row]
    # for row in artist_list:
    #   for list_of_names in row   ^^^^^^ basically that
    #
#
#
# def get_proxy():
#     proxy_data = GetProxy()
#     proxy_list = proxy_data.generate_proxy()
#
#



#     print(similar_artists)
#     print(artist_tags)




# def by_genre_lastfm():
#     user_input_genre = input("Which genre out of those do you want? make sure you type it right!\n")
#     artists_on_tag_list = artist_data_lastfm.get_tag_artists(user_input_genre)
#     artists_on_tag = flattening_list(artists_on_tag_list)
#     with open(f"same_genre_artists_as_{user_choice}", "w", encoding="utf-8") as file:
#         for artist in artists_on_tag:
#             file.write(f"{artist}\n")
#     print(artists_on_tag)




# def by_top_single_rym():
#     pass


# def by_top_album_rym():
#     pass


# def by_lists_rym():
#     pass


# user_choice = input("What is the artist you're looking for?\n")
# if " " in user_choice:
#     user_choice = user_choice.replace(" ", "+")
#     print(user_choice)


# artist_data_lastfm = GrabArtist(user_choice)
# artist_data_lastfm.get_similar_artists




# artist_data_rym = rym_data.RateYourMusic(user_choice)
# top_singles = artist_data_rym.get_top_single()






##Making ui


open_window = MainWindow()



open_window.mainloop()





