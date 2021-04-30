# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:56:04 2021

@author: max
"""

import tkinter as tk

window = tk.Tk()
window.title("Covid-19 Simulator")
window.columnconfigure([0, 1], minsize=150)
window.rowconfigure([0, 1, 2], minsize=50)
window.resizable(width=False, height=False)

# frm_greeting=tk.Frame(master=window)
lbl_greeting = tk.Label(master=window, text="Hello and welcome to our covid 19 simulator!")

# frm_info=tk.Frame(master=window)
lbl_info = tk.Label(master=window, text="This simulator will put you in the position of the PM during the pandemic and test your abilities to run the country.")

def _continue():
    print("Hello world")
    
btn_continue = tk.Button(
    master=window,
    text="Continue",
    command= _continue()
)

def _quit():
        window.quit()     # stops mainloop
        # window.destroy()
        print("Goodbye!")

btn_quit = tk.Button(
    master=window,
    text="Quit",
    command= _quit()
)

lbl_greeting.grid(row=0, column=0, padx=10)
lbl_info.grid(row=1, column=0, padx=10)
btn_continue.grid(row=2, column=0, padx=10, pady=10)
btn_quit.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()