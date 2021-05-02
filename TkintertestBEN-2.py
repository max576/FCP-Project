# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:38:24 2021

@author: max
"""

##bitvalues
DISTANCING = 1
FACEMASKS = 2
PUBS = 4
NON_ESSENTIAL = 8 
BORDERS = 16
LOCKDOWN = 32

INVALID_ENTRY = 0


# Afew examples of programs using Tkinter taken from https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app it's helpful to have this open whilst looking at the examples.
# Comment and uncomment examples one at a time

# Always keep imports active
import tkinter as tk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


class epidemic_control:
    def __init__(self, controlid,name, prompt, bitvalue, weight):
        # Basic simulation parameters:
        self.controlid = controlid
        self.name = name
        self.prompt = prompt
        self.bitvalue = bitvalue
        self.weight = weight

def initialize_controls(controls):
    
    ###IMPROVEMENT - provide csv initialize option for control list parameters
    
    controls.append(epidemic_control(0,"Distancing","Enter [Y] to implement 2 metre social distancing rules, [N] to ignore this measure : ",DISTANCING,[0.3,0.1,1.0,1.0,0.6,0.2]))
    controls.append(epidemic_control(1,"Facemasks","Enter [Y] to implement facemasks, [N] to ignore this measure : ",FACEMASKS,[0.2,0.3,0.8,0.9,0.6,0.2]))
    controls.append(epidemic_control(2,"Early Closing","Enter [Y] to implement pubs early closing, [N] to ignore this measure : " ,PUBS,[1.5,1.5,1.5,1.5,1.5,1.5]))
    controls.append(epidemic_control(3,"Close Non-essential Shops","Enter [Y] to close non-essential shops, [N] to ignore this measure : ",NON_ESSENTIAL,[0.8,0.7,0.9,0.8,0.6,0.7]))
    controls.append(epidemic_control(4,"Close International Borders","Enter [Y] to close international borders, [N] to ignore this measure : ",BORDERS,[0.2,0.1,0.6,0.8,0.9,0.9]))
    controls.append(epidemic_control(5,"Total Lockdown","Enter [Y] to implement a full National Lockdown, [N] to ignore this measure : ",LOCKDOWN,[0.4,0.1,0.3,0.6,0.7,0.9]))

class period:
    def __init__(self, controlid,name, story, r_rate):
        # Basic simulation parameters:
        self.controlid = controlid
        self.name = name
        self.story = story
        self.r_rate = r_rate
        
def initialize_periods(periods):

    ###IMPROVEMENT - provide csv import option for period content

    periods.append(period(0,"Period 1 - Happy New Year!","Well, not quite so happy, but the year has begun nevertheless. \nAs PM, you have been alerted of a new virus spreading across the UK with a naturally fluctuating R-Rate. \nScientists will be simultaneously working on producing a vaccine for the public which will be ready at the end of the year, \nwhilst reporting the new R-Rate to the Health secretary every two months, who will then report to you. Your task over the following year is to review the current R rate every two months and implement \ndifferent restrictions/safety measures in attempt to reduce the R rate, and save lives! Although, it is important to consider the economic repercussions of each parameter in place, as each your budget is finite. Furthermore, \nan additional segment of social context will be given to you for each period in hope to influence your decisions further.\n\n",1.4))
    periods.append(period(1,"Period 2 - March and April","Place holder for story for period 2", 1.2))
    periods.append(period(2,"Period 3","Place holder for story for period 3 ", 1.3))
    periods.append(period(3,"Period 4","Place holder for story for period 4 ", 1.1))
    periods.append(period(4,"Period 5","Place holder for story for period 5 ", 1.3))
    periods.append(period(5,"Period 6","Place holder for story for period 6 ", 1.5))
        
#def drawUI(window,ctl,periods):


def plot_and_move_next(fig, canvas, cb_var):
   #plot chart for this period
    n = 0
    cb = 0
    while n != len(cb_var):
      cb = cb + cb_var[n].get()  
      n += 1
    
    userchoice.append(cb)

    plot(fig, canvas, userchoice)
    #move to next period, sey screen prompts
    cnt_current_period.set(cnt_current_period.get() + 1)
    if cnt_current_period.get() == 6 : 
        cnt_current_period.set(5)
        next_button["state"] = "disabled"
        next_button["text"] = "Finished!"
        
    print(cnt_current_period.get())
    pName.set(periods[cnt_current_period.get()].name + "\n\n" + periods[cnt_current_period.get()].story)
          
def nextPeriod(event=None):
    cnt_current_period.set(cnt_current_period.get() + 1)
    if cnt_current_period.get() > 6 : cnt_current_period.set(6)
    
def currPeriod(event=None):
    return cnt_current_period.get()


def plot(fig, canvas, userchoice):

    x = []
    y = []
    i=0
    while i != len(userchoice):   
       x.append(userchoice[i])
       print (x)
       print (i)
       print (periods[i].r_rate)
       print (ctl[i])
       if (userchoice[i] & ctl[i].bitvalue) != 0 : print (ctl[i].weight[i]) 
       i += 1


    x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    y = [0, 0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1.0]


	# list of squares
    y = [i**currPeriod() for i in range(101)]

	# adding the subplot
    plot1 = fig.add_subplot(111)

	# plotting the graph
    plot1.plot(y)

	# creating the Tkinter canvas
	# containing the Matplotlib figure

    canvas.draw()

	# placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

	# creating the Matplotlib toolbar
# 	toolbar = NavigationToolbar2Tk(canvas,
# 								window)
# 	toolbar.update()

	# placing the toolbar on the Tkinter window
# 	canvas.get_tk_widget().pack()




###############
#
#  M A I N
#
###############

ctl = []
periods = []
initialize_controls(ctl)
initialize_periods(periods)

window = tk.Tk() #creates a window
cnt_current_period = tk.IntVar()
pName = tk.StringVar()
userchoice = []


window.title("COVID Simulator")
window.geometry('1000x1200')

   
frame1 = tk.Frame(master=window, width=50, height=50, bg="red")
frame1.pack(fill=tk.BOTH)

label1 = tk.Label(master=frame1, bg="red", fg="white", text = "Hello and welcome to our covid 19 simulator") 
label1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="white")
frame2.pack()

pName.set(periods[cnt_current_period.get()].name + "\n\n" + periods[cnt_current_period.get()].story)    
label2 = tk.Label(master=frame2, textvariable=pName)
label2.pack()


frame3 = tk.Frame(master=window, width=50, height=50, bg="blue")
frame3.pack(fill=tk.BOTH)

label3 = tk.Label(master=frame3, text = "Choose which safety measures you wish to implement during this period")
label3.pack()

frame4 = tk.Frame(master=window, width=50, height=50)
frame4.pack(fill=tk.BOTH)
   
i = 0
# List (0-5) to hold each checkbox selection
cb_var = []
while i != len(ctl):
    #declare list items as int values 
    cb_var.append(tk.IntVar())
    #create checkboxes, onvalue = bitvalue & name from epidemic_control, store value in cb_var
    chk = tk.Checkbutton(master=frame4, onvalue=ctl[i].bitvalue, offvalue=0, text=ctl[i].name, variable=cb_var[i])
    chk.pack(fill=tk.BOTH)
    i += 1
 
# the figure that will contain the plot
fig = Figure(figsize = (5, 5), dpi = 100)
canvas = FigureCanvasTkAgg(fig, master = window)

#tk.Label(window, textvariable=cnt_current_period).pack()
next_button = tk.Button(window, text="Next Period", command=lambda: plot_and_move_next(fig, canvas,cb_var), fg="dark green", bg = "white")
next_button.pack()
tk.Button(window, text="Quit", command=window.destroy, fg="dark green", bg = "white").pack() 

 
##for x in userchoice:
##     print("\nuser choice: " +str(x))

window.mainloop() #used to make the program work