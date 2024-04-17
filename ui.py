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



        #Images

        self.danbo_face_image = CTkImage(Image.open("./images/button.png"), size=(30, 20))
        self.danbo = CTkImage(Image.open("./images/danbo.png"), size=(158, 119))
        self.yotsuba_singing = CTkImage(Image.open(".   /images/yotsuba_singing.png"), size=(120, 120))
        self.yotsuba_logo = CTkImage(Image.open("./images/yotsuba_png.png"), size=(100, 100))
        self.yotsuba_image = CTkImage(Image.open("./images/yotsuba.png"), size=(150, 150))
        self.spotify_image = CTkImage(Image.open("./images/spotify.png"), size=(30, 30))
        self.scrapingbee_image = CTkImage(Image.open("./images/bee.png"), size=(30, 30))

