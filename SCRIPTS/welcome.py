# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:02:40 2021

@author: max and ben (legends)
"""

#!/usr/bin/python
import tkinter as tk
from PIL import ImageTk, Image

def display_welcome_screen():
    
     #creates a window
    welcome_window = tk.Tk() 
    
    welcome_window.title("COVID Simulator")
    welcome_window.tk.call('wm', 'iconphoto', welcome_window._w, tk.PhotoImage(file='GRAPHICS/icon.png'))
    welcome_window.geometry('1200x1200')
    welcome_frame1 = tk.Frame(master=welcome_window, width=50, height=50, bg="red")
    welcome_frame1.pack(fill=tk.BOTH)
    
    welcome_label1 = tk.Label(master=welcome_frame1, bg="red", fg="white", text = "Hello and welcome to our covid 19 simulator") 
    welcome_label1.pack()
    
    welcome_frame2 = tk.Frame(master=welcome_window, width=50, height=50, bg="white")
    welcome_frame2.pack()
    
    welcome_label2 = tk.Label(master=welcome_frame2, text="Welcome" + "\n\n Happy New Year! Well, not quite so happy, but the year has begun nevertheless. As PM, you have\n been alerted of a new virus spreading across the UK with a naturally fluctuating R-Rate. Scientists\n will be simultaneously working on producing a vaccine for the public which will be ready at the end\n of the year, whilst reporting the new R-Rate to the Health secretary every two months, who\n will then report to you. Your task over the following year is to review the current R rate every two\n months and implement different restrictions/safety measures in attempt to reduce the R rate, and\n save lives! Although, it is important to consider the economic repercussions of each parameter in\n place, as each your budget is finite. Furthermore, an additional segment of social context will be\n given to you for each period in hope to influence your decisions further.\n\n\n Every period you will be asked to implement any / a combination of parameters.")
    welcome_label2.pack()
    
    welcome_frame3 = tk.Frame(master=welcome_window, width=90, height=60,)
    welcome_frame3.pack()
    
    image1 = Image.open("GRAPHICS/virus.png")
    virus = ImageTk.PhotoImage(image1)
    label1 = tk.Label(master = welcome_frame3, image = virus)
    label1.image = virus
    label1.pack()
    
    
    tk.Button(welcome_window, text="Start!", command=welcome_window.destroy, fg="dark green", bg = "white").pack()
    #display welcome_window, destroyed by button press above
    # tk.Button(welcome_window, text="Quit", command=welcome_window.quit(), fg="dark green", bg = "white").pack() 
    welcome_window.mainloop() 
