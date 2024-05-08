import tkinter as tk
from customtkinter import *
import customtkinter
from PIL import Image


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        # Set appearance and color theme first
        


        # Initialize frames dictionary before using it in show_frame method
        self.frames = {}
        for Page in (StartPage, PageOne):
            frame = Page(self)
            self.frames[Page] = frame
            frame.pack(fill="both", expand=True)
            frame.pack_forget() 
            # frame.pack(pady=1, padx=1, fill="both", expand=True)

        # Now it's safe to show the initial frame
        self.show_frame(StartPage)

        # Set window size and title
        self.geometry('500x400')
        self.title('Spotify ya hallo!')

    def show_frame(self, page_class):
        for frame in self.frames.values():
            frame.pack_forget()  # This effectively hides the frame
        frame = self.frames[page_class]
        print('switched frames')
        frame.pack(pady=1, padx=1, fill="both", expand=True)    




class StartPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)


        yotsuba_image = CTkImage(Image.open("./lastfm_scraper/images/yotsuba.png"), size=(150, 150))
        yotsuba = customtkinter.CTkLabel(self, text="", fg_color="transparent",
                                             image=yotsuba_image)
        yotsuba.place(x=175, y=40)




        #SCRAPINGBEE ENTRY AND LOGO
        scrapingbee_image = CTkImage(Image.open("./lastfm_scraper/images/bee.png"), size=(30, 30))

        scrapingbee_label = customtkinter.CTkLabel(self, text="", fg_color="transparent", image=scrapingbee_image)
        scrapingbee_label.place(x=70, y=193)

        self.scrapingbee = customtkinter.CTkEntry(self, placeholder_text="BEEKEY", width=300, height=40, corner_radius=50)
        self.scrapingbee.place(x=110, y=190)


        #SPOTIFY ENTRY AND LOGO
        self.spotify_image = CTkImage(Image.open("./lastfm_scraper/images/spotify.png"), size=(30, 30))

        spotify_label = customtkinter.CTkLabel(self, text="", fg_color="transparent", image=self.spotify_image)
        spotify_label.place(x=70, y=245)


        self.spotify = customtkinter.CTkEntry(self, placeholder_text="SPOTIFYKEY", width=300, height=40, corner_radius=50)
        self.spotify.place(x=110, y=240)





        self.danbo_face_image = CTkImage(Image.open("./lastfm_scraper/images/button.png"), size=(30, 20))
        login_button = customtkinter.CTkButton(self, text="", image=self.danbo_face_image, fg_color="transparent",
                                                   border_color="white", hover_color="grey", border_width=1, corner_radius=5,
                                                   height=40, width=60, command=lambda: master.show_frame(PageOne))
        login_button.place(x=220, y=300)


class PageOne(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.place(x=2, y=10)


        yotsuba_logo = CTkImage(Image.open("./lastfm_scraper/images/yotsuba_png.png"), size=(100, 100))
        yotsuba = CTkLabel(self, text="", fg_color="transparent",
                                             image=yotsuba_logo)
        yotsuba.place(x=25, y=20)



        
        self.danbo_face_image = CTkImage(Image.open("./lastfm_scraper/images/button.png"), size=(30, 20))

        go_back_button = CTkButton(self, text="", image=self.danbo_face_image,
                                                   fg_color="transparent", corner_radius=5,
                                                   border_color="white", hover_color=("gray70", "gray30"),
                                                   height=40, command=lambda: master.show_frame(StartPage))
        go_back_button.place(x=0, y=300)



        lastfm_button = CTkButton(self, corner_radius=5, height=40,
                                                         border_spacing=10, text="LASTFM",
                                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         command=self.on_lastfm_button)
        lastfm_button.place(x=0, y=150)



        spotify_button = CTkButton(self, corner_radius=5, height=40,
                                                         border_spacing=10, text="Spotify",
                                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         command=self.on_spotify_button)
        spotify_button.place(x=0, y=232)




        self.rym_button = CTkButton(self, corner_radius=5, height=40,
                                                      border_spacing=10, text="RYM",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      command=lambda:self.on_rym_button())
        self.rym_button.place(x=0, y=190)



        self.label = CTkLabel(self, text="")
        self.label.pack()


        self.on_lastfm_button()

    def on_lastfm_button(self):
        

        danbo_image = CTkImage(Image.open("./lastfm_scraper/images/danbo.png"), size=(158, 119))
        self.label.configure(text='')
        





        
    def on_rym_button(self):
        self.label.configure(text='You clicked page TWo BUTTON')
    
    def on_spotify_button(self):
        self.label.configure(text='You clicked page blablabla')



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()