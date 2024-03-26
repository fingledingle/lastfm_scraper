from last_fm_data import GrabArtist





#I KNOW I COULD PUT THAT ON LASTFMDATA I KNOW THANK YOU FOR NOTICING
def flattening_list(artist_list):
    return [list_of_names for row in artist_list for list_of_names in row]
    # for row in artist_list:
    #   for list_of_names in row   ^^^^^^ basically that

artist_data = GrabArtist()
artist_list = artist_data.get_artists()
similar_artists = flattening_list(artist_list)


print(similar_artists)


