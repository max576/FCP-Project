# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:59:55 2021

@author: max and ben (legends)
"""

#!/usr/bin/python
import tkinter as tk
from PIL import ImageTk, Image



def display_results(): 
    results_window = tk.Tk() 
    
    results_window.title("COVID Simulator")
    results_window.tk.call('wm', 'iconphoto', results_window._w, tk.PhotoImage(file='GRAPHICS/icon.png'))
    results_window.geometry('1200x1200')
    results_frame1 = tk.Frame(master=results_window, width=50, height=50, bg="red")
    results_frame1.pack(fill=tk.BOTH)
    
    results_label1 = tk.Label(master=results_frame1, bg="red", fg="white", text = "Thank you for using our covid 19 simulator") 
    results_label1.pack()
    
    results_frame2 = tk.Frame(master=results_window, width=50, height=50, bg="white")
    results_frame2.pack()
    
    results_label2 = tk.Label(master=results_frame2, text="Results" + "\n\n Congratulations! You have now completed the simulation.\n The cumulative death toll and some analysis of the total expenditure is shown below.\n")
    results_label2.pack()
    

    results_frame3 = tk.Frame(master=results_window, width=50, height=50,)
    results_frame3.pack()
    
    image1 = Image.open("PLOTS/death.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(master = results_frame3, image = test)
    label1.image = test
    label1.pack()
    
    results_frame4 = tk.Frame(master=results_window, width=75, height=50,)
    results_frame4.pack()
    
    image2 = Image.open("PLOTS/pie.png")
    test2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(master = results_frame4, image = test2)
    label2.image = test2
    label2.pack()
    
    results_frame5 = tk.Frame(master=results_window, width=50, height=50, bg="white")
    results_frame5.pack()
    
    results_label5 = tk.Label(master=results_frame5, text="Click the 'Quit' button to end the program or replay to give it another go.")
    results_label5.pack()
    
    def replay():
        results_window.destroy()
        from Main import replay
        replay()

    
    tk.Button(results_window, text="Quit", command=results_window.destroy, fg="dark green", bg = "white").pack() 
    #display welcome_window, destroyed by button press above
    
    tk.Button(results_window, text="replay", command=replay, fg="dark green", bg = "white").pack() 

    results_window.mainloop() 
    






