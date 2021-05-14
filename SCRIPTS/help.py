# -*- coding: utf-8 -*-
"""
Created on Fri May 14 02:10:08 2021

@author: max
"""

#!/usr/bin/python
import tkinter as tk
from PIL import ImageTk,Image

def Get_help():
    
     #creates a window
    help_window = tk.Tk() 
    
    help_window.title("COVID Simulator")
    # help_window.tk.call('wm', 'iconphoto', help_window._w, tk.PhotoImage(file='GRAPHICS/help_icon.png'))
    help_window.geometry('800x550')
    # help_window.configure(bg='white')
    
    help_frame1 = tk.Frame(master=help_window, width=50, height=50, bg="red")
    help_frame1.pack(fill=tk.BOTH)
    
    help_label1 = tk.Label(master=help_frame1, bg="red", fg="white", text = "Help me!") 
    help_label1.pack()
    
    help_frame2 = tk.Frame(master=help_window, width=50, height=50, bg="white")
    help_frame2.pack()
    
    help_label2 = tk.Label(master=help_frame2, text="\n\nAs PM, you have\n been alerted of a new virus spreading across the UK with a naturally fluctuating R-Rate. Scientists\n will be simultaneously working on producing a vaccine for the public which will be ready at the end\n of the year, whilst reporting the new R-Rate to the Health secretary every two months, who\n will then report to you. Your task over the following year is to review the current R rate every two\n months and implement different restrictions/safety measures in attempt to reduce the R rate, and\n save lives! Although, it is important to consider the economic repercussions of each parameter in\n place, as each your budget is finite. Furthermore, an additional segment of social context will be\n given to you for each period in hope to influence your decisions further.\n\n\n Every period you will be asked to implement any / a combination of the following parameters:\n\n\n 2 metre social distancing for anyone outside of your living circle / support bubble.\n This works in conjunction with the bligation to wear face coverings in any indoor public space, and outdoors when breaching social distancing.\n\n Closing all pubs and restaurants by 10pm.\n\n Closing all non-essential shops.\n Closing international borders for all visitors. Nobody comes in, nobody comes out. Overseas shipments for essential items i.e. food may still proceed.\n\n Full national lockdown. Everyone must stay at home and only leave the house for 1 hour of\n individual exercise, purchasing essential goods from a supermarket, and taking yourself\n or a direct family member to the hospital when seriously ill. Everyone who is able\n to work from home should continue to work, otherwise a furlough scheme will be in\n place (which will provide any individual with 80% of their standard wage / salary).")
    help_label2.pack()
    
    tk.Button(help_window, text="I understand!", command=help_window.destroy, fg="dark green", bg = "white").pack()


    help_window.mainloop() 
    


