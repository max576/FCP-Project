# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:56:04 2021

@author: max
"""

import tkinter as tk

window = tk.Tk()
window.title("Covid-19 Simulator")

frm_greeting=tk.Frame(master=window)
lbl_greeting = tk.Label(master=frm_greetingw, text="Hello and welcome to our covid 19 simulator!")

frm_info=tk.Frame(master=window)
lbl_info = tk.Label(master=frm_info, text="This simulator will put you in the position of the PM during the pandemic and test your abilities to run the country.")

btn_continue = tk.Button(
    master=window,
    text="Continue",
    command=print("Hello World")
)

btn_quit = tk.Button(
    master=window,
    text="Quit",
    command=print("Goodbye!"
)

frm_greeting.grid(row=0, column=0, padx=10)
frm_info.grid(row=1, column=0, padx=10)
btn_continue.grid(row=2, column=0, padx=10, pady=10)
btn_quit.grid(row=2, column=1 padx=10, pady=10)

window.mainloop()