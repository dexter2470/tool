import customtkinter as c
from CTkMessagebox import CTkMessagebox
import sqlite3
import PIL as imagetk
import requests

c.set_appearance_mode('dark')
c.set_default_color_theme('green')


if __name__=="__main__":
    window=c.CTk()
    # window.geometry('800x600')
    window.title('WASP BLOG')
    window.maxsize(900, 700)
    window.minsize(800, 600)
    # window.iconbitmap('')


    #frame sections
   
    navbar_frames = c.CTkFrame(window, fg_color=("#722F37"), width= 800,height=100,corner_radius=0 )
    navbar_frames.grid(row=0, column=0, sticky= 'nsew', columnspan=2)

    menu_frames = c.CTkFrame(window, fg_color="green", corner_radius=0, width=100, height=500)
    menu_frames.grid(row=1, column=0, sticky='nsew')

    content_frames = c.CTkFrame(window, fg_color='white', corner_radius=0, width=700)
    content_frames.grid(row=1, column=1, sticky='nsew')


    navbar_label = c.CTkLabel(navbar_frames, text="Welcome to WASP's Blog \nNews,Entertainment,Lifestyle,Inspiration and yes...Gossip")
    navbar_label.grid(row=0,column=0)
    
    
    # menu buttons
    home_button =c.CTkButton(menu_frames, text="Home")
    home_button.grid(row=0, column=0,pady=(10, 30))

    news_button =c.CTkButton(menu_frames, text="News")
    news_button.grid(row=1,column=0, pady=(0,30) )

    music_button =c.CTkButton(menu_frames, text="Music")
    music_button.grid(row=2, column=0, pady=(0, 30))

    video_button =c.CTkButton(menu_frames, text= "Video")
    video_button.grid(row=3, column=0, pady=(0, 30))

    lifestyle_button =c.CTkButton(menu_frames, text="Lifesytle")
    lifestyle_button.grid(row=4, column=0, pady=(0, 30))

    politics_buttton =c.CTkButton(menu_frames, text= "Politics")
    politics_buttton.grid(row=5, column=0, pady=(0, 30))
    
    schools_button =c.CTkButton(menu_frames, text="Education")
    schools_button.grid(row=6, column=0, pady=(0, 30))
   
    sports_button =c.CTkButton(menu_frames, text="Agriculture")
    sports_button.grid(row=6, column=0, pady=(0, 30))
   
    religion_button =c.CTkButton(menu_frames, text="Religion")
    religion_button.grid(row=6, column=0, pady=(0, 30))

     #column and row configuration
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)
    


    window.mainloop()
