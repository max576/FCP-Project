  
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:59:55 2021
@author: max and ben (legends)
"""

#!/usr/bin/python
import tkinter as tk
import PIL
from PIL import ImageTk, Image
from matplotlib.figure import Figure
# from Draft2 import plot, econ, pie
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


def econ():
    from draft2 import e
    return e


def display_results(): 
    results_window = tk.Tk() 
    
    results_window.title("COVID Simulator")
    results_window.tk.call('wm', 'iconphoto', results_window._w, tk.PhotoImage(file='icon.png'))
    results_window.geometry('1200x1000')
    results_frame1 = tk.Frame(master=results_window, width=50, height=50, bg="red")
    results_frame1.pack(fill=tk.BOTH)
    
    results_label1 = tk.Label(master=results_frame1, bg="red", fg="white", text = "Thank you for using our covid 19 simulator") 
    results_label1.pack()
    
    results_frame2 = tk.Frame(master=results_window, width=50, height=50, bg="white")
    results_frame2.pack()
    
    results_label2 = tk.Label(master=results_frame2, text="Results [" + str(econ()) + "]\n\n blah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\n")
    results_label2.pack()
    

    results_frame3 = tk.Frame(master=results_window, width=50, height=50,)
    results_frame3.pack()
    
    
    # from Draft2 import plot
    # fig = Figure(figsize = (7.5, 5), dpi = 105)
    # canvas = FigureCanvasTkAgg(fig, master = results_window)
    
    # canvas.draw()
    # canvas.get_tk_widget().pack()
    
    

    
    image1 = Image.open("plot1.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(master = results_frame3, image = test)
    label1.image = test
    label1.pack()
    
    results_frame4 = tk.Frame(master=results_window, width=50, height=50,)
    results_frame4.pack()
    
    image2 = Image.open("plot2.jpg")
    test2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(master = results_frame4, image = test2)
    label2.image = test2
    label2.pack()

    
    tk.Button(results_window, text="Quit", command=results_window.destroy, fg="dark green", bg = "white").pack() 
    #display welcome_window, destroyed by button press above
    results_window.mainloop() 
    
