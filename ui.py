import tkinter as tk
from customtkinter import *
import customtkinter
from PIL import Image
from last_fm_data import GrabArtist



print('poopy')

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class MainWindow(CTk):
    def __init__(self):
        super().__init__()






        #Setting the attributes for the startingpage keys
        self.scrapingbee_key = ''
        self.spotify_key = ''


        # Set appearance and color theme first



        # Initialize frames dictionary before using it in show_frame method
        self.frames = {}    
        for Page in (StartPage, PageOne):
            frame = Page(self)
            self.frames[Page] = frame
            frame.pack(fill="both", expand=True)
            frame.pack_forget() 
            
        
        print(self.frames)



        # Set window size and title
        self.geometry('500x400')
        self.title('Spotify ya hallo!')



        # Now it's safe to show the initial frame
        self.show_frame(StartPage)


    def show_frame(self, page_class):
        #For the frame in self.frames.value() < - basically the values inside the self.frames dictionary
        print("Attempting to show frame:", page_class.__name__)
        for frame in self.frames.values():
            print("Hiding frame:", frame)
            frame.place_forget()  # This effectively hides the frame
        #frame will be = the dictionary value that is = page_class (page_class being the Class passed through self.show_frame)    
        frame = self.frames[page_class]
        #Places the frame that is = the value inside the dic that we previously got 
        print("Showing frame:", frame)
        frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=1, relheight=1)

    





class StartPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        print('currently at page start_page')

        yotsuba_image = CTkImage(Image.open("./images/yotsuba.png"), size=(150, 150))
        yotsuba = customtkinter.CTkLabel(self, text="", fg_color="transparent",
                                             image=yotsuba_image)
        yotsuba.place(x=175, y=40)




        #SCRAPINGBEE ENTRY AND LOGO
        scrapingbee_image = CTkImage(Image.open("./images/bee.png"), size=(30, 30))

        scrapingbee_label = customtkinter.CTkLabel(self, text="", fg_color="transparent", image=scrapingbee_image)
        scrapingbee_label.place(x=70, y=193)

        self.scrapingbee = customtkinter.CTkEntry(self, placeholder_text="BEEKEY", width=300, height=40, corner_radius=50)
        self.scrapingbee.place(x=110, y=190)


        #SPOTIFY ENTRY AND LOGO
        self.spotify_image = CTkImage(Image.open("./images/spotify.png"), size=(30, 30))

        spotify_label = customtkinter.CTkLabel(self, text="", fg_color="transparent", image=self.spotify_image)
        spotify_label.place(x=70, y=245)


        self.spotify = customtkinter.CTkEntry(self, placeholder_text="SPOTIFYKEY", width=300, height=40, corner_radius=50)
        self.spotify.place(x=110, y=240)





        self.danbo_face_image = CTkImage(Image.open("./images/button.png"), size=(30, 20))
        login_button = customtkinter.CTkButton(self, text="", image=self.danbo_face_image, fg_color="transparent",
                                                   border_color="white", hover_color="grey", border_width=1, corner_radius=5,
                                                   height=40, width=60, command=lambda: self.login(master))
        login_button.place(x=220, y=300)




    #Settings the keys as master so they can be used around the whole program
    def login(self, master):
        master.scrapingbee_key = self.scrapingbee.get() 
        master.spotify_key = self.spotify.get()
        master.show_frame(PageOne)


    # def getkey(self, master):
    #     return (master.scrapingbee_key, master.spotify_key)
        


class PageOne(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(x=2, y=10)
        self.configure(fg_color = 'grey')
    
        #printing the key for test purposes
        print("ScrapingBee Key:", master.scrapingbee_key)
        print("Spotify Key:", master.spotify_key)
        

        self.sub_frames = {}
        for ServiceFrame in (LastFmFrame, SpotifyFrame, RymFrame):
            frame = ServiceFrame(self)  

            self.sub_frames[ServiceFrame] = frame
            frame.place(x=2, y=10)
            frame.place_forget()


        self.create_service_button('LastFM', LastFmFrame, 150)
        self.create_service_button('Spotify', SpotifyFrame, 232)
        self.create_service_button('RYM', RymFrame, 190)

        self.show_sub_frames(LastFmFrame)


        yotsuba_logo = CTkImage(Image.open("./images/yotsuba_png.png"), size=(100, 100))
        yotsuba = CTkLabel(self, text="", fg_color="transparent",
                                             image=yotsuba_logo)
        yotsuba.place(x=25, y=20)

        
        self.danbo_face_image = CTkImage(Image.open("./images/button.png"), size=(30, 20))

        go_back_button = CTkButton(self, text="", image=self.danbo_face_image,
                                                   fg_color="transparent", corner_radius=5,
                                                   border_color="white", hover_color=("gray70", "gray30"),
                                                   height=40, command=lambda: master.show_frame(StartPage))
        go_back_button.place(x=0, y=300)



    def create_service_button(self, text, frame_class, y_position):
        button = CTkButton(
            self,
            text=text,
            command= lambda: self.show_sub_frames(frame_class),
            corner_radius=5,
            height=40,
            fg_color='transparent',
            hover_color=("gray70", "gray30")
            )
        button.place(x=0, y=y_position)
        
    def show_sub_frames(self, frame_class):
        for frame in self.sub_frames.values():
            frame.place_forget()
        frame = self.sub_frames[frame_class]
        frame.place(x=160, y=4, relwidth=0.65, relheight=0.98)
        


class LastFmFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)    
        

        def segmented_button_value(value):
            print(value)
            if value == 'similar artists':
                print(f'the key test {master.master.scrapingbee_key}')
                self.similar_artists = CTkEntry(self, placeholder_text='artist name', width=150, corner_radius=50)
                self.similar_artists.place(relx=0.5, y=290, anchor='center')

                start_search_button = CTkButton(self,
                                text="", border_color="white", 
                                hover_color="grey", border_width=1,
                                image=self.danbo_face_image, 
                                width=60, height=40,
                                command=lambda: last_fm_search(self.similar_artists.get(), 
                                                                self.page_quantity.get(),
                                                                self.songs_quantity.get(),
                                                                master.master.scrapingbee_key))
                start_search_button.place(relx=0.5, y= 340, anchor='center')

            else:
                print(f'the key test {master.master.spotify_key}')
                self.similar_genre = CTkEntry(self, placeholder_text='genre name', width=150, corner_radius=50)
                self.similar_genre.place(relx=0.5, y=290, anchor='center')

                start_search_button = CTkButton(self,
                                text="", border_color="white", 
                                hover_color="grey", border_width=1,
                                image=self.danbo_face_image, 
                                width=60, height=40)
                                # command=lambda: last_fm_search(self.similar_genre.get(), 
                                #                                 self.page_quantity.get(),
                                #                                 self.songs_quantity.get(),
                                #                                 master.master.scrapingbee_key))
                start_search_button.place(relx=0.5, y= 340, anchor='center')








        self.danbo_face_image = CTkImage(Image.open("./images/button.png"), size=(30, 20))


        self.danbo = CTkImage(Image.open("./images/danbo.png"), size=(158, 119))
        danbo_header = CTkLabel(self,
                                text="",
                                fg_color="transparent",
                                image=self.danbo
                                )
        danbo_header.place(anchor='center', relx=0.5, y=80)   



        methods = CTkSegmentedButton(self, 
                                     values=['similar artists', 'same genre'],
                                     width=160, command=segmented_button_value
                                     )
        methods.place(anchor='center', relx=0.5, y=170)
        methods.set('methods')


    
        page_quantity_label = CTkLabel(self, text='QT.Pages', fg_color="transparent")
        page_quantity_label.place(relx= 0.3, y=190)

        songs_quantity_label = CTkLabel(self, text='QT.Songs', fg_color="transparent")
        songs_quantity_label.place(relx= 0.55, y=190)



        self.page_quantity = CTkEntry(self, width=45, corner_radius=50)
        self.page_quantity.place(relx=0.33, y=220)

        self.songs_quantity = CTkEntry(self, width=45, corner_radius=50)
        self.songs_quantity.place(relx=0.55, y=220)



        #CAnvas here probably



###########################H--Handling the search--####################################
        def last_fm_search(similar_artist, page_quantity, songs_quantity, scrapingbee_key):
            print(f'The artist is: {similar_artist}\n The quantity is: {page_quantity}\n The key is: {scrapingbee_key}')


################################################################################################
            grab_artists = GrabArtist(similar_artist, str(scrapingbee_key), page_quantity)
            getting_similar_artists = grab_artists.get_similar_artists()
            if getting_similar_artists == 'False':
                #Do spotify stuff
                print('hey my name is jefferson')

            # artist_names = [list_of_names for row in unorganized_artist_list for list_of_names in row]


            # # artist_tags = grab_artists.get_genre()

            # with open(f"similar_artists_to_{similar_artist}", "w", encoding="utf-8") as file:
            #     for artist in artist_names:
            #         file.write(f"{artist}\n")   



            #Spotify stuff
        
 ####################################################################################




        #CAnvas here probably



    


        






class SpotifyFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = CTkLabel(self, text="Spotify Frame")
        label.pack()


class RymFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = CTkLabel(self, text='RYM Frame')
        label.pack()




# if __name__ == "__main__":
# app = MainWindow()
# app.mainloop()