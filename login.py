from customtkinter import *
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox
import json


class MainWindow:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        self.window = CTk()
        self.window.geometry("500x400")
        self.window.title("Spotify ya' hallo!")


    def program_windows(self):

        def button(spotify, scrapingbee, key_frame):
            key_frame.destroy()
            main_page()
            print(spotify)


        def lastfm_button():

            def same_genre():
                pass






            self.menu_frame = CTkFrame(self.window, height=390, width=352, corner_radius=25)
            self.menu_frame.place(x=146, y=5)

            def similar_artists():
                self.similar_artist = customtkinter.CTkEntry(master=self.menu_frame, placeholder_text="", width=150,
                                                            corner_radius=50)
                self.similar_artist.place(x=101, y=270)

            similar_artists()



            self.danbo = CTkImage(Image.open("./images/danbo.png"), size=(158, 119))
            self.yotsuba = customtkinter.CTkLabel(self.menu_frame, text="", fg_color="transparent",
                                             image=self.danbo)
            self.yotsuba.place(x=105, y=55)




            self.methods = customtkinter.CTkSegmentedButton(master=self.menu_frame, values=["similar artists", "same genre"], width=160)
            self.methods.place(x=96, y=180)
            self.methods.set("methods")



            self.artist_label = customtkinter.CTkLabel(master=self.menu_frame, text="QT.Artist", fg_color="transparent")
            self.artist_label.place(x=120, y=220)
            self.artist_quantity = customtkinter.CTkEntry(master=self.menu_frame, placeholder_text="", width=45, corner_radius=50)
            self.artist_quantity.place(x=125, y=245)




            self.song_label = customtkinter.CTkLabel(master=self.menu_frame, text="QT.Songs", fg_color="transparent")
            self.song_label.place(x=200, y=220)
            self.song_quantity = customtkinter.CTkEntry(master=self.menu_frame, placeholder_text="", width=45,
                                                          corner_radius=50)
            self.song_quantity.place(x=205, y=245)














        def rym_button():
            pass

        def spotify_button():
            pass



        def main_page():
            lastfm_button()

            #PSEUDO LEFT SIDE
            self.menu_frame = CTkFrame(self.window, height=380, width=140, corner_radius=25)
            # self.main_frame.pack(pady=1, padx=0, fill= Y, expand=True, x=0)
            self.menu_frame.place(x=2, y=10)




            self.yotsuba_logo = CTkImage(Image.open("./images/yotsuba_png.png"), size=(100, 100))
            yotsuba = customtkinter.CTkLabel(self.menu_frame, text="", fg_color="transparent",
                                             image=self.yotsuba_logo)
            yotsuba.place(x=25, y=20)








            self.lastfm_button = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40,
                                                         border_spacing=10, text="LASTFM",
                                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         command=lastfm_button)

            self.lastfm_button.place(x=0, y=150)

            self.rym_button = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="RYM",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      command=rym_button)
            self.rym_button.place(x=0, y=190)

            self.spotify = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40,
                                                   border_spacing=10, text="Add song to spotify",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   command=spotify_button)
            self.spotify.place(x=0, y=300)


            #PSEUDO RIGHT SIDE








        def keys_window():


            self.key_frame = CTkFrame(self.window)
            self.key_frame.pack(pady=1, padx=1, fill="both", expand=True)


            #Yotsuba LOL
            self.yotsuba_image = CTkImage(Image.open("./images/yotsuba.png"), size=(150, 150))
            yotsuba = customtkinter.CTkLabel(self.key_frame, text="", fg_color="transparent",
                                                       image=self.yotsuba_image)
            yotsuba.place(x=175, y=40)




            #SCRAPINGBEE ENTRY AND LOGO

            self.scrapingbee_image = CTkImage(Image.open("./images/bee.png"), size=(30, 30))
            scrapingbee_label = customtkinter.CTkLabel(self.key_frame, text="", fg_color="transparent", image=self.scrapingbee_image)
            scrapingbee_label.place(x=70, y=193)


            self.scrapingbee = customtkinter.CTkEntry(master=self.key_frame, placeholder_text="BEEKEY", width=300, height=40, corner_radius=50)
            self.scrapingbee.place(x=110, y=190)




            #SPOTIFY ENTRY AND LOGO

            self.spotify_image = CTkImage(Image.open("./images/spotify.png"), size=(30, 30))
            spotify_label = customtkinter.CTkLabel(self.key_frame, text="", fg_color="transparent", image=self.spotify_image)
            spotify_label.place(x=70, y=245)


            self.spotify = customtkinter.CTkEntry(master=self.key_frame, placeholder_text="SPOTIFYKEY", width=300, height=40, corner_radius=50)
            self.spotify.place(x=110, y=240)







            #Button
            self.danbo_face_image = CTkImage(Image.open("./images/button.png"), size=(30, 20))

            login_button = customtkinter.CTkButton(self.key_frame, text="", image=self.danbo_face_image, fg_color="transparent",
                                                   border_color="white", hover_color="grey", border_width=1, corner_radius=5,
                                                   height=40, width=60, command=lambda: button(self.spotify.get(), self.scrapingbee.get(), self.key_frame))
            login_button.place(x=220, y=300)


        keys_window()

        self.window.mainloop()