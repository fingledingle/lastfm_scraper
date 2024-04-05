

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




def LOGIN():

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):  
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True) 


    def continue_button_clicked():
        f=open(relative_to_assets("details.txt"), "w")
        bee=entry_3.get()
        spotify=entry_4.get()
        if bee=="" or spotify=="":
            messagebox.showerror("Error", "Please fill all the details retard")
        else:
            #add these into f :
            f.write(bee+"\n")
            f.write(spotify+"\n")
            f.close()
            a=open(relative_to_assets("auth.txt"), "w")
            a.write("TRUE")  
            a.close()
            window.destroy()

    def access_details():
        f=open(relative_to_assets("details.txt"), "r")
        name=f.readline()
        email=f.readline()
        return name, email


    window = Tk()

    window.geometry("930x506")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 506,
        width = 930,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        469.0,
        0.0,
        1012.0,
        506.0,
        fill="#FFFFFF",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        676.3636474609375,
        331.00000000000006,
        image=entry_image_1
    )


    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        676.3636474609375,
        224.00000000000006,
        image=entry_image_2
    )

    canvas.create_text(
        527.0,
        306.00000000000006,
        anchor="nw",
        text="Spotify Token",
        fill="#3E9752",
        font=("Montserrat Bold", 15 * -1)
    )

    canvas.create_text(
        527.0,
        204.00000000000006,
        anchor="nw",
        text="ScrapingBee Token",
        fill="#3E9752",
        font=("Montserrat Bold", 15 * -1)
    )

    canvas.create_text(
        517.0,
        66.00000000000006,
        anchor="nw",
        text="こんにちは、ニガちゃん！",
        fill="#3E9752",
        font=("Montserrat Bold", 26 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: continue_button_clicked(),
        relief="flat"
    )
    button_1.place(
        x=641.0,
        y=412.00000000000006,
        width=190.0,
        height=48.0
    )



    rounded_background = round_rectangle(20.0, 17.00, 469, 491, radius=50, fill="#3E9752")

    canvas.create_text(
        85.0,
        77.00000000000006,
        anchor="nw",
        text="jeffbot",
        fill="#FFFFFF",
        font=("Montserrat Bold", 50 * -1)
    )

    canvas.create_text(
        518.0,
        109.00000000000006,
        anchor="nw",
        text="maks sure tocken-san warks thanki",
        fill="#3E9752",
        font=("Montserrat SemiBold", 16 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        675.0,
        241.00000000000006,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#EFEFEF",
        highlightthickness=0,
        font=("Montserrat SemiBold", 16 * -1),
        foreground="#3E9752"
    )
    entry_3.place(
        x=525.0,
        y=225.0,
        width=290.0,
        height=30.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        676.0,
        342.00000000000006,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#EFEFEF",
        highlightthickness=0,
        font=("Montserrat SemiBold", 16 * -1),
        foreground="#3E9752"
    )
    entry_4.place(
        x=525.0,
        y=325.00000000000006,
        width=290.0,
        height=30.0
    )


    canvas.create_text(
        90.0,
        162.00000000000006,
        anchor="nw",
        text="Welcome To jeffreyBottey V1 \nplease do not share this app \nmuch appreciated \nwith love\nJeff.\n",
        fill="#FFFFFF",
        font=("Montserrat Regular", 18 * -1)
    )

    canvas.create_text(
        90.0,
        431.00000000000006,
        anchor="nw",
        text= ("©") + " fingledingle, 2024",
        fill="#FFFFFF",
        font=("Montserrat Bold", 18 * -1)
    )


    window.resizable(False, False)
    window.mainloop()


LOGIN()