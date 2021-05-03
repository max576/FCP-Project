# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:38:24 2021

@author: bendy
"""

##bitvalues
DISTANCING = 1
FACEMASKS = 2
PUBS = 4
NON_ESSENTIAL = 8 
BORDERS = 16
LOCKDOWN = 32

INVALID_ENTRY = 0
MAGIC_NUMBER = 10000


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
        #controls effect on R-Rate
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
    def __init__(self, controlid, r_rate, name, story):
        # Basic simulation parameters:
        self.controlid = controlid
        #seasonal adjustment to R-Rate
        self.r_rate = r_rate
        self.name = name
        self.story = story
        
def initialize_periods(periods):

    ###IMPROVEMENT - provide csv import option for period content

    periods.append(period(0, 1.4,"Period 1 - Happy New Year!","Well, not quite so happy, but the year has begun nevertheless. \nAs PM, you have been alerted of a new virus spreading across the UK with a naturally fluctuating R-Rate. \nScientists will be simultaneously working on producing a vaccine for the public which will be ready at the end of the year, \nwhilst reporting the new R-Rate to the Health secretary every two months, who will then report to you. Your task over the following year is to review the current R rate every two months and implement \ndifferent restrictions/safety measures in attempt to reduce the R rate, and save lives! Although, it is important to consider the economic repercussions of each parameter in place, as each your budget is finite. Furthermore, \nan additional segment of social context will be given to you for each period in hope to influence your decisions further.\n\n"))
    periods.append(period(1, 1.2,"Period 2 - March and April","Place holder for story for period 2"))
    periods.append(period(2, 1.3,"Period 3","Place holder for story for period 3 "))
    periods.append(period(3, 1.3,"Period 4","Place holder for story for period 4 "))
    periods.append(period(4, 1.1,"Period 5","Place holder for story for period 5 "))
    periods.append(period(5, 1.5,"Period 6","Place holder for story for period 6 "))
    
        
#def drawUI(window,ctl,periods):

def display_welcome_screen():
    
    #creates a window
    welcome_window = tk.Tk() 
    
    welcome_window.title("COVID Simulator")
    welcome_window.geometry('1200x1000')
    welcome_frame1 = tk.Frame(master=welcome_window, width=50, height=50, bg="red")
    welcome_frame1.pack(fill=tk.BOTH)
    
    welcome_label1 = tk.Label(master=welcome_frame1, bg="red", fg="white", text = "Hello and welcome to our covid 19 simulator") 
    welcome_label1.pack()
    
    welcome_frame2 = tk.Frame(master=welcome_window, width=50, height=50, bg="white")
    welcome_frame2.pack()
    
    welcome_label2 = tk.Label(master=welcome_frame2, text="Welcome" + "\n\n blah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\nblah blah blah blah blah blah blah blah\n")
    welcome_label2.pack()
    
    
    tk.Button(welcome_window, text="Start!", command=welcome_window.destroy, fg="dark green", bg = "white").pack()
    #display welcome_window, destroyed by button press above
    welcome_window.mainloop() 

def plot_and_move_next_period(fig, canvas, cb_var):
   #plot chart for this period
    n = 0
    cb = 0
    while n != len(cb_var):
      cb = cb + (cb_var[n].get())  
      n += 1
      
    print (cb)
    
    userchoice.append(cb)

    plot(fig, canvas, userchoice)
    

    #final period? disable button otherwese set next period and  load  next period instructions
    if current_period.get() == len(periods)-1 : 
        next_button["state"] = "disabled"
        next_button["text"] = "Finished!"
    else:
        current_period.set(current_period.get() + 1)
        pName.set(periods[current_period.get()].name + "\n\n" + periods[current_period.get()].story)
          
    
def currPeriod(event=None):
    return current_period.get()

def magic_number():
    return MAGIC_NUMBER


def plot(fig, canvas, userchoice):

    #Instanticate list for periods (x) , and player guess(y) and actuals(y2)
    x = []
    y = []
    y2 = []
    x.append(0)
    y.append(0)
    y2.append(0)
    r=0
    a=0
    
    
    print("=====================================")    
    print("Plotting with these values")
    print("userchoice : " + str(userchoice))
    print("Current Period : " + str(currPeriod()))

    uc=0
    #For the number of periods enteres so far...
    while uc != len(userchoice):   
       #get the actual rate for the period, store as actual
       r = periods[uc].r_rate
       a = r
       print("------------------------")
       print ("uc = " + str(uc))
       print ("x = " + str(x))
       print ("period [" + str(currPeriod()) +"]  r_rate= " + str(periods[uc].r_rate))
       
       p=0
       #for each parameter, if the player has enabled the check box adjust r-rate its weight
       while p != len(ctl):
           print ("Period [" + str(uc) + "] Parameter [" + str(ctl[p].name) +  "] weighting for period [" + str(currPeriod()) + "] is [" + str(ctl[p].weight[currPeriod()] ) + "]" )
           if (userchoice[uc] & ctl[p].bitvalue) != 0 : r = r * ctl[p].weight[currPeriod()] 
           print ("Cumulative r rate" + str(r))
           p += 1
       
       uc += 1
       #add to x & y's'
       x.append(uc)
       y.append(r * magic_number())
       y2.append(a * magic_number())
       print(x)
       print(y)
       print (y2)

 

    # adding the subplot

    plot1 = fig.add_subplot(111)
 	# plotting the graph

    plot1.plot(x, y, label = "Your Guess")
    plot1.plot(x, y2, label = "Actuals")

    plot1.legend(['Your Guess','Actuals']) 
    plot1.set_xlabel('Period')
    plot1.set_title('Death Rate after parameter ')

    #plot1.plot(y)

	# creating the Tkinter canvas
	# containing the Matplotlib figure

    canvas.draw()
    canvas.get_tk_widget().pack()
    
    # plot1.remove()
    # del plot1
	# placing the canvas on the Tkinter window
    #canvas.get_tk_widget().pack()

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

#instantiate list variables to store control measure & period objects
ctl = []
periods = []
actuals = []
#populate these lists with static data
initialize_controls(ctl)
initialize_periods(periods)
#Instantiate a list to store the players selection of 
#control measures for each period (strored as bitvalue)
userchoice = []

#call welcome screen function, destroy window on button press
display_welcome_screen()

#Instantiate tkinter window
window = tk.Tk() 
#Instantiate tkinter int to identify current period 
#and current perriod instructions
current_period = tk.IntVar()
pName = tk.StringVar()

####Tkinter window and widget definitions

window.title("COVID Simulator")
#width x height
window.geometry('1200x1000')

# create frame / label for  title banner 
frame1 = tk.Frame(master=window, width=50, height=200, bg="red")
frame1.pack(fill=tk.BOTH)

label1 = tk.Label(master=frame1, bg="red", fg="white", text = "Hello and welcome to our covid 19 simulator") 
label1.pack()

# create frame / label for Period instructions
frame2 = tk.Frame(master=window, width=50, height=50, bg="white")
frame2.pack()

#load values for 
pName.set(periods[current_period.get()].name + "\n\n" + periods[current_period.get()].story)    
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
    #declare list items as int values to store state 
    cb_var.append(tk.IntVar())
    #create checkboxes, onvalue = bitvalue & name from epidemic_control, store value in cb_var
    chk = tk.Checkbutton(master=frame4, onvalue=ctl[i].bitvalue, offvalue=0, text=ctl[i].name, variable=cb_var[i])
    chk.pack(fill=tk.BOTH)
    i += 1
 
# the figure that will contain the plot
#fig = plt.Figure(figsize=(5,4), dpi=100)
fig = Figure(figsize = (5, 5), dpi = 100)
canvas = FigureCanvasTkAgg(fig, master = window)

#tk.Label(window, textvariable=current_period).pack()
next_button = tk.Button(window, text="Next Period", command=lambda: plot_and_move_next_period(fig, canvas,cb_var), fg="dark green", bg = "white")
next_button.pack()
tk.Button(window, text="Quit", command=window.destroy, fg="dark green", bg = "white").pack() 

 
##for x in userchoice:
##     print("\nuser choice: " +str(x))

window.mainloop() #used to make the program work