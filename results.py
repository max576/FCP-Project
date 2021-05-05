# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:59:55 2021

@author: max
"""

#!/usr/bin/python
import tkinter as tk
import PIL
from PIL import ImageTk, Image

def display_results(): 
    results_window = tk.Tk() 
    
    results_window.title("COVID Simulator")
    # results_window.tk.call('wm', 'iconphoto', results_window._w, tk.PhotoImage(file='icon.png'))
    results_window.geometry('1200x1000')
    results_frame1 = tk.Frame(master=results_window, width=50, height=50, bg="red")
    results_frame1.pack(fill=tk.BOTH)
    
    results_label1 = tk.Label(master=results_frame1, bg="red", fg="white", text = "Thank you for using our covid 19 simulator") 
    results_label1.pack()
    
    results_frame2 = tk.Frame(master=results_window, width=50, height=50, bg="white")
    results_frame2.pack()
    
    results_label2 = tk.Label(master=results_frame2, text="Results" + "\n\n blah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\n")
    results_label2.pack()
    
    # image1 = Image.open("results.jpg")
    # test = ImageTk.PhotoImage(image1) 
    
    results_frame3 = tk.Frame(master=results_window, width=50, height=50,)
    results_frame3.pack()
    
    # fig = Figure(figsize = (7.5, 5), dpi = 105)
    # canvas = FigureCanvasTkAgg(fig, master = window)
    
    image1 = Image.open("results.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(master = results_frame3, image = test)
    label1.image = test
    label1.pack()
    # Position image
    # label1.place(x=1, y=2)
    
    tk.Button(results_window, text="Quit", command=results_window.destroy, fg="dark green", bg = "white").pack() 
    #display welcome_window, destroyed by button press above
    results_window.mainloop() 
    
    # from PIL import ImageTk,Image.
    # window = tk.Tk()
    # canvas = tk.Canvas(window, width = 300, height = 300)
    # canvas.pack()
    # imageFile = "Aaron.jpg"
    
    # window.im1 = Image.open(imageFile)
    
    
    # raw_input()
    # img = tk.Image(Image.open('results.png'))
    # canvas.create_image(20, 20, anchor=NW, image=img)
    # window.mainloop()
    
    # import tkinter
    # from tkinter import *
    # from PIL import Image, ImageTk
    # root = Tk()
    # # Create a photoimage object of the image in the path
    # image1 = Image.open("results.jpg")
    # test = ImageTk.PhotoImage(image1)
    # label1 = tkinter.Label(image=test)
    # label1.image = test
    # # Position image
    # label1.place(x=1, y=2)
    # root.mainloop()

