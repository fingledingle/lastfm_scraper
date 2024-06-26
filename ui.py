import tkinter as tk
from customtkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import Image
from last_fm_data import GrabArtist
from spotify import Spotify_thingy




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

        self.resizable(False, False)


        # Set window size and title
        self.geometry('500x400')
        self.title('Spotify ya hallo!')



        # Now it's safe to show the initial frame
        self.show_frame(StartPage)


    def show_frame(self, page_class):
        #For the frame in self.frames.value() < - basically the values inside the self.frames dictionary
        for frame in self.frames.values():
            frame.place_forget()  # This effectively hides the frame
        #frame will be = the dictionary value that is = page_class (page_class being the Class passed through self.show_frame)    
        frame = self.frames[page_class]
        #Places the frame that is = the value inside the dic that we previously got 
        frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=1, relheight=1)

    





class StartPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        

        yotsuba_image = CTkImage(Image.open("./images/yotsuba.png"), size=(150, 150))
        yotsuba = customtkinter.CTkLabel(self, text="", fg_color="transparent",
                                             image=yotsuba_image)
        yotsuba.place(x=175, y=20)




        #SCRAPINGBEE ENTRY AND LOGO
        scrapingbee_image = CTkImage(Image.open("./images/bee.png"), size=(30, 30))

        scrapingbee_label = customtkinter.CTkLabel(self, text="", fg_color="transparent", image=scrapingbee_image)
        scrapingbee_label.place(x=70, y=173)

        self.scrapingbee = customtkinter.CTkEntry(self, placeholder_text="BEEKEY", width=300, height=40, corner_radius=50)
        self.scrapingbee.place(x=110, y=170)


        #SPOTIFY ENTRY AND LOGO
        self.spotify_image = CTkImage(Image.open("./images/spotify.png"), size=(30, 30))

        spotify_label = customtkinter.CTkLabel(self, text="", fg_color="transparent", image=self.spotify_image)
        spotify_label.place(x=70, y=250)


        self.spotify_client_id = customtkinter.CTkEntry(self, placeholder_text="client id", width=300, height=40, corner_radius=50)
        self.spotify_client_id.place(x=110, y=220)

        self.spotify_secret_id = customtkinter.CTkEntry(self, placeholder_text="secret id", width=300, height=40, corner_radius=50)
        self.spotify_secret_id.place(x=110, y=270)





        self.danbo_face_image = CTkImage(Image.open("./images/button.png"), size=(30, 20))
        login_button = customtkinter.CTkButton(self, text="", image=self.danbo_face_image, fg_color="transparent",
                                                   border_color="white", hover_color="grey", border_width=1, corner_radius=5,
                                                   height=40, width=60, command=lambda: self.login(master))
        login_button.place(x=220, y=330)




    #Settings the keys as master so they can be used around the whole program
    def login(self, master):
        master.scrapingbee_key = self.scrapingbee.get() 
        master.spotify_key = [self.spotify_client_id.get(), self.spotify_secret_id.get()]
        master.show_frame(PageOne)



class PageOne(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # self.place(x=5, y=10)
        self.configure(corner_radius=25)
        

        self.sub_frames = {}
        for ServiceFrame in (LastFmFrame, SpotifyFrame): #RymFrame
            frame = ServiceFrame(self)  

            self.sub_frames[ServiceFrame] = frame
            frame.place(x=2, y=10)
            frame.place_forget()


        self.create_service_button('LastFM', LastFmFrame, 150)
        self.create_service_button('Spotify', SpotifyFrame, 232)
        # self.create_service_button('RYM', RymFrame, 190)

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
        frame.place(relx=0.28, y=8, relwidth=0.71, relheight=0.96)
        


class LastFmFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)    
        
        self.configure(corner_radius=25)
        def segmented_button_value(value):
            print(value)
            if value == 'similar artists':
                self.similar_artists = CTkEntry(self, placeholder_text='artist name', width=150, corner_radius=50)
                self.similar_artists.place(relx=0.5, y=290, anchor='center')

                start_search_button = CTkButton(self,
                                text="", border_color="white", 
                                hover_color="grey", border_width=1,
                                image=self.danbo_face_image, 
                                width=60, height=40,
                                command=lambda: last_fm_search(user_choice = self.similar_artists.get(), 
                                                               page_quantity= self.page_quantity.get(),
                                                               song_quantity= self.song_quantity.get(),
                                                               scrapingbee_key= master.master.scrapingbee_key,
                                                               spotify_key=master.master.spotify_key,
                                                               choice_type = 'similar artists'))
                start_search_button.place(relx=0.5, y= 340, anchor='center')

            else:
                self.similar_genre = CTkEntry(self, placeholder_text='genre name', width=150, corner_radius=50)
                self.similar_genre.place(relx=0.5, y=290, anchor='center')

                start_search_button = CTkButton(self,
                                text="", border_color="white", 
                                hover_color="grey", border_width=1,
                                image=self.danbo_face_image, 
                                width=60, height=40,
                                command=lambda: last_fm_search(user_choice = self.similar_genre.get(), 
                                                                page_quantity= self.page_quantity.get(),
                                                                song_quantity= self.song_quantity.get(),
                                                                scrapingbee_key= master.master.scrapingbee_key,
                                                                spotify_key=master.master.spotify_key,
                                                                choice_type = 'same genre'))
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

        self.song_quantity = CTkEntry(self, width=45, corner_radius=50)
        self.song_quantity.place(relx=0.55, y=220)






###########################H--Handling the search--(similar artist)####################################
        def last_fm_search(user_choice, page_quantity, song_quantity,  scrapingbee_key, choice_type, spotify_key):
            page_quantity = int(page_quantity)
            song_quantity = int(song_quantity)


            if song_quantity == '' or page_quantity == '':
                CTkMessagebox(title='HEY!!!', message='It appears you left some of the fields empty!!', icon="cancel")
            elif page_quantity >= 27:
                CTkMessagebox(title='HEY!!!', message="Woah that's a lot of pages! try to lower it to a number below 27", icon="cancel")


            else:
                #Check if the  choice was genre method or similar artist method
                if choice_type == 'similar artists':
                    print(f'The artist is: {user_choice}\n The quantity is: {page_quantity}\n The keys are\n for scrapingbee: {scrapingbee_key}\n for spotify: {spotify_key}')
                

                    if " " in user_choice:
            
                        user_choice = user_choice.replace(" ", "+")

                    grab_artists = GrabArtist(user_choice=user_choice, scrapingbee_key=str(scrapingbee_key), spotify_key=spotify_key, page_quantity=page_quantity, song_quantity=song_quantity)
                    getting_similar_artists = grab_artists.get_similar_artists()



                elif choice_type == 'same genre':
                    print(f'The genre is: {user_choice}\n The quantity is: {page_quantity}\n The keys are\n for scrapingbee: {scrapingbee_key}\n for spotify: {spotify_key}')

                    if " " in user_choice:
                        
                        user_choice = user_choice.replace(" ", "+")

                    grab_artists = GrabArtist(user_choice=user_choice, scrapingbee_key=str(scrapingbee_key), spotify_key=spotify_key, page_quantity=page_quantity, song_quantity=song_quantity)
                    getting_same_genre = grab_artists.get_tag_artists()

################Spotify stuff###################
            
        
 ####################################################################################



class SpotifyFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)


        def send_to_spotify(user_choice, method):


            # client_id=master.master.spotify_key[0]
            # client_secret=master.master.spotify_key[1]

            if method == 'manual':

                artists = user_choice.split('\n')
                artists.pop()



            elif method == 'automatic':

                artists = [index.strip() for index in user_choice]
                print(master.naster.spotify_key[0], master.master.spotify_key[1])


            spotify = Spotify_thingy(artists_names=artists, song_quantity=5, client_id=master.master.spotify_key[0], client_secret=master.master.spotify_key[1], methods='single page')
            start_searching = spotify.search_and_add()



        def Upload_action():
            filename = filedialog.askopenfilename()
            print('Selected:', filename)
            return filename

        def select_file(file_type):
            if file_type == 'txt':
                global selected_text
                selected_text = Upload_action()
                if selected_text:
                    with open (selected_text) as file:
                        self.artists = file.readlines()
                        
                        try:
                            self.placing_artists_on_screen = CTkLabel(self, text=f'artists:\n\n{self.artists[0]}\n{self.artists[1]}\n{self.artists[2]}\n...woah so many')
                            self.placing_artists_on_screen.place(anchor='center', relx=0.25, y=250)
                        except IndexError:
                            self.placing_artists_on_screen = CTkLabel(self, text=f'artists: \n\n not that many artists!\n but we will work with it!')
                            self.placing_artists_on_screen.place(anchor='center', relx=0.25, y=250)
                        return self.artists




        yotsuba_singing_image = CTkImage(Image.open("./images/yotsuba_singing.png"), size=(130, 160))
        self.clover = CTkImage(Image.open('./images/awesome.png'), size=(20,20))
        self.danbo_face_image = CTkImage(Image.open("./images/button.png"), size=(30, 20))



        self.configure(corner_radius=25)
        
        yotsuba_singing = CTkLabel(self, image=yotsuba_singing_image,
                                   text='', fg_color='transparent' )

        yotsuba_singing.place(relx=0.55, y=225)

        





        def segmented_button_value(value):
            if value == 'automatic':

                try:
                    self.user_entry.place_forget()
                    self.start_search_user_input.place_forget()
                    self.write_it_down.place_forget()
                except AttributeError:
                    print('well this doesnt exist yet')



                self.choose_file = CTkLabel(self, text='Choose your file!',
                               fg_color = 'transparent')
                self.choose_file.place(anchor='center', relx=0.25, y=100)

                self.attach_file = CTkButton(self, text='', border_color='green',
                                        border_width = 1, width=60, height=40,
                                        fg_color='transparent', 
                                        image=self.clover,
                                        command= lambda: select_file('txt'))
                self.attach_file.place(anchor='center', relx=0.25, y=140)



                self.send_artists = CTkLabel(self, text='Start search!', 
                                        fg_color = 'transparent')
                self.send_artists.place(anchor='center', relx=0.75, y=100)

                self.start_search_button = CTkButton(self,
                                text="", border_color="green", 
                                border_width=1,
                                image=self.danbo_face_image, 
                                width=60, height=40,
                                command=lambda: send_to_spotify(user_choice=self.artists, method='automatic'))
                self.start_search_button.place(anchor='center', relx=0.75, y=140)
                



            else:

                    
                try:
                    self.placing_artists_on_screen.place_forget()
                except AttributeError:
                    print('this doesnt exist yet!')
                try:
                    self.choose_file.place_forget()
                    self.attach_file.place_forget()
                    self.send_artists.place_forget()
                    self.start_search_button.place_forget()
                except AttributeError:
                    print('well this doesnt either')
            
                


                self.write_it_down = CTkLabel(self, text='write it yourself then!',
                               fg_color = 'transparent')
                self.write_it_down.place(anchor='center', relx=0.5, y=90)

                
                self.user_entry = CTkTextbox(self, width=200, height=100, border_width=3, font=('Arial', 10, 'bold'))
                self.user_entry.place(relx=0.5, y=150, anchor='center')

                

                self.start_search_user_input = CTkButton(self,
                                text="", border_color="green", 
                                border_width=1,
                                image=self.danbo_face_image, 
                                width=60, height=40,
                                command= lambda: send_to_spotify(self.user_entry.get('1.0', 'end'), method='manual'))
                self.start_search_user_input.place(anchor='center', relx=0.3, y=230)





        
        
        methods = CTkSegmentedButton(self, 
                                     values=['automatic', 'manual'],
                                     width=100, command=segmented_button_value)
        methods.place(anchor='center', relx=0.5, y=50)
        methods.set('methods')

        
        






# class RymFrame(CTkFrame):
#     def __init__(self, master):
#         super().__init__(master)
#         label = CTkLabel(self, text='RYM Frame')
#         label.pack()
