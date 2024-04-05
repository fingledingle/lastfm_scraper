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
            for widget in key_frame.winfo_children():
                widget.destroy()
            print(spotify)
            main_page()



        def main_page():
            self.navigation_frame = CTkFrame(self.window)
            self.navigation_frame.pack(pady=1, padx=1, fill="both", expand=True)
            pass



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