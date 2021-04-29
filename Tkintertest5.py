# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:38:24 2021

@author: max
"""

# Afew examples of programs using Tkinter taken from https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app it's helpful to have this open whilst looking at the examples.
# Comment and uncomment examples one at a time

# Always keep imports active
import tkinter as tk
import random


window = tk.Tk() #creates a window

# 1- Me messing around with it to create an example program (probably doesn't work)

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
    
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)

# frame1 = tk.Frame(master=window, width=50, height=50, bg="red")
# frame1.pack(fill=tk.BOTH)

# label1 = tk.Label(master=frame1, text = "Hello and welcome to our covid 19 simulator") 
# label1.pack()

# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack(fill=tk.BOTH)

# label2 = tk.Label(text = "This simulator will put you in the position of the PM during the pandemic and test your abilities to run the country")
# label2.pack()

# frame3 = tk.Frame(master=window, width=50, height=50, bg="blue")
# frame3.pack(fill=tk.BOTH)

# label3 = tk.Label(text = "Type Y to continue ot N to quit")
# label3.pack()

# entry = tk.Entry(width=40)
# entry.pack()

# answer = entry.get()

# if answer == "N" window.destroy():
#     else print("thank you")

# 2- Simple counter good example for using buttons

# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"


# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"

# window = tk.Tk()

# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# btn_decrease.grid(row=0, column=0, sticky="nsew")

# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)

# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")

# 3- Dice roll simulator (Needs random to be imported)

# def roll():
#     lbl_result["text"] = str(random.randint(1, 6))

# window = tk.Tk()
# window.columnconfigure(0, minsize=150)
# window.rowconfigure([0, 1], minsize=50)

# btn_roll = tk.Button(text="Roll", command=roll)
# lbl_result = tk.Label()

# btn_roll.grid(row=0, column=0, sticky="nsew")
# lbl_result.grid(row=1, column=0)

# 4- Temperature Converter good example for using the users input value in further code

# def fahrenheit_to_celsius():
#     """Convert the value for Fahrenheit to Celsius and insert the
#     result into lbl_result.
#     """
#     fahrenheit = ent_temperature.get()
#     celsius = (5/9) * (float(fahrenheit) - 32)
#     lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# # Set-up the window
# window = tk.Tk()
# window.title("Temperature Converter")
# # window.resizable(width=False, height=False)

# # Create the Fahrenheit entry frame with an Entry
# # widget and label in it
# frm_entry = tk.Frame(master=window)
# ent_temperature = tk.Entry(master=frm_entry, width=10)
# lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# # Layout the temperature Entry and Label in frm_entry
# # using the .grid() geometry manager
# ent_temperature.grid(row=0, column=0, sticky="e")
# lbl_temp.grid(row=0, column=1, sticky="w")

# # Create the conversion Button and result display Label
# btn_convert = tk.Button(
#     master=window,
#     text="\N{RIGHTWARDS BLACK ARROW}",
#     command=fahrenheit_to_celsius
# )
# lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# # Set-up the layout using the .grid() geometry manager
# frm_entry.grid(row=0, column=0, padx=10)
# btn_convert.grid(row=0, column=1, pady=10)
# lbl_result.grid(row=0, column=2, padx=10)

# Run the application

window.mainloop() #used to make the program work