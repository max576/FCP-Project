# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:38:24 2021
@author: max and ben (legends)
"""

#!/usr/bin/python

##bitvalues
DISTANCING = 1
PUBS = 2
NON_ESSENTIAL = 4 
BORDERS = 8
LOCKDOWN = 16

INVALID_ENTRY = 0
MAGIC_NUMBER = 10000


# A few examples of programs using Tkinter taken from https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app it's helpful to have this open whilst looking at the examples.
# Comment and uncomment examples one at a time

# Always keep imports active
import tkinter as tk
# from welcome import display_welcome_screen
# from results import display_results
import numpy as np
import random
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


class epidemic_control:
    def __init__(self, controlid,name, prompt, bitvalue, weight, cost):
        # Basic simulation parameters:
        self.controlid = controlid
        self.name = name
        self.prompt = prompt
        self.bitvalue = bitvalue
        #controls effect on R-Rate
        self.weight = weight
        self.cost = cost

def initialize_controls(controls):
    
    ###IMPROVEMENT - provide csv initialize option for control list parameters
    
    controls.append(epidemic_control(0,"Distancing & Facemasks","Although this is the most basic measure, it is one of the most effective at inhibiting the spread of disease. However, it may affect people's mental wellbeing as you're unable to hug your loved ones and it may affect the economy as shops and restaurants are unlikely to do as well if fewer people are allowed in them as they must be spread further apart. ",DISTANCING,[0.6,0.7,0.9,0.9,0.8,0.6], 3900000000))
    controls.append(epidemic_control(1,"Early Closing","This will significantly affect the economy as there won't be as much revenue coming in to the pubs. Also, the average British person won't be too happy about this." ,PUBS,[1.7,1.7,1.7,1.7,1.7,1.7], 1900000000))
    controls.append(epidemic_control(2,"Close Non-essential Shops","Shops play a huge role in the country's economy - if they were to close, many people would lose their jobs and have to go on furlough, and the government would suffer, as would the mental wellbeing of the people who no longer have a day job, and some independent shops may have to close permanently due to the lack of income. However, indoor spaces are a breeding ground for viruses like Covid-19. ",NON_ESSENTIAL,[0.7,0.7,0.9,0.9,0.8,0.7], 16000000000))
    controls.append(epidemic_control(3,"Close International Borders","Although closing the borders will make it much harder for Covid-19 and its new variants to spread to the UK, it will have a huge impact on the airline industry. It also stops family and friends who live abroad from seeing each other which will affect their wellbeing, as well as stop people from taking nice mental breaks to go on holiday.",BORDERS,[0.7,0.7,0.7,0.7,0.7,0.7], 64000000000))
    controls.append(epidemic_control(4,"Total Lockdown","A full scale lockdown is the best measure to control the spread of the virus, but would have devastating effects both socially and econmically: children won't get their necessary social interactions and their learning will be affected, people won't get to see their family and friends, which is an integral part of human nature, and won't be able to go to work; many people would have to work from home or go on furlough, and the government, as well as business owners for example would struggle financially, just to name a few. ",LOCKDOWN,[0.4,0.4,0.7,0.8,0.6,0.3], 146000000000))
    

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

    periods.append(period(0, 3.2,"Period 1 - January / February","The Health Secretary has informed you that the initial R-Rate is 3.2\n\n Of course, it is very cold throughout January and February and people are naturally coming down\n with the flu over winter. As a rule, spending is low across the UK in retail, but the public still desire\n eating out and drinking in cosy pubs. Although, it is proven that keeping pubs open has a direct\n correlation against the spread of virus. The health secretary advises against keeping cosy pubs open\n\n"))
    periods.append(period(1, 2.7,"Period 2 - March and April","Place holder for story for period 2"))
    periods.append(period(2, 2.1,"Period 3","Place holder for story for period 3 "))
    periods.append(period(3, 1.5,"Period 4","Place holder for story for period 4 "))
    periods.append(period(4, 2.0,"Period 5","Place holder for story for period 5 "))
    periods.append(period(5, 2.9,"Period 6","Place holder for story for period 6 "))
    
# def exit():
#     exit()
    
        
#def drawUI(window,ctl,periods):
    
def on_enter(event):
    # # ctl = []
    # i = 0
    # #List (0-5) to hold each checkbox selection
    # #cb_var = []
    # while i != len(ctl):
    #     label4.configure(text=ctl[i].prompt) 
    label4.configure(text="willy")
def on_leave(event):
    label4.configure(text="")    


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
        next_button["text"] = "Results"
        next_button["state"] = "enabled"
        # next_button.configure(text = "Results", command = display_results()
        # window.destroy()

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
    plot1.plot(x, y2, label = "Unhinged")

    plot1.legend(['Your Guess','Unhinged']) 
    plot1.set_xlabel('Period')
    plot1.set_ylabel('Death toll (people)')
    plot1.set_title('Death Toll after parameter ')


    #plot1.plot(y)

	# creating the Tkinter canvas
	# containing the Matplotlib figure

    canvas.draw()
    canvas.get_tk_widget().pack()
    
   
    if currPeriod() > 0:  plot1.remove()
    if currPeriod() > 0: del plot1
    plt.savefig('plot1.jpg')
    
    # plot1.remove()
    # del plot1
    
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

    

# Economic cost of each parameter, this function will save the cost of each period, to then be totalled for the final results and called by the pie chart function
def econ():
    
    uc=0
    e=0
    
    #For the number of periods enteres so far...
    while uc != len(userchoice):   
       #get the actual cost for the period, store as actual
       e = ctl[uc].cost
      
       print("------------------------")
       print ("uc = " + str(uc))
       print ("Cost " + str(ctl[uc].cost))
       print ("ctl " + str(len(ctl)))

       
       p=0
       #for each parameter, if the player has enabled the check box accumulate the cost
       while p != len(ctl):
           if (userchoice[uc] & ctl[p].bitvalue) != 0 : e = e + ctl[p].cost 
           print ("Accumulated Cost" + str(e))
           print ("p" + str(p))

           p += 1          
    uc += 1      
    print ("uc" + str(uc))
    return e 

    
    

def pie():
    
    uc = 0
    while uc != len(userchoice):
        c = ctl[uc].bitvalue
        d = ctl[uc].cost
        
        # print("------------------------")
        # print ("uc = " + str(uc))
        # print ("Cost " + str(ctl[uc].bitvalue)
        # print ("ctl " + str(len(ctl)))
        
    
    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.axis('equal')
    controls = ['Distancing & Facemasks', 'Early Closing', 'Close Non-essential Shops', 'Close International Borders', 'Total Lockdown']
    costs = [10000,2000,30000,40000,50000]
    ax.pie(costs, labels = controls,autopct='%1.2f%%')
    plt.title("Total Debt:" + str(econ()))
    if currPeriod() >= 5: plt.savefig('plot2.jpg')
    # plt.show()
    
    
    
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
from welcome import display_welcome_screen
display_welcome_screen()


#Instantiate tkinter window
window = tk.Tk() 
#Instantiate tkinter int to identify current period 
#and current perriod instructions
current_period = tk.IntVar()
pName = tk.StringVar()

####Tkinter window and widget definitions

window.title("COVID Simulator")
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='icon.png'))
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

frame4 = tk.Frame(master=window, width=75, height=50)
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
    label4 = tk.Label(master=frame4, text="")
    label4.pack()
    chk.bind("<Enter>", on_enter)
    chk.bind("<Leave>", on_leave)
    #

 
# the figure that will contain the plot
#fig = plt.Figure(figsize=(5,4), dpi=100)
fig = Figure(figsize = (7.5, 5), dpi = 105)
canvas = FigureCanvasTkAgg(fig, master = window)

#tk.Label(window, textvariable=current_period).pack()
next_button = tk.Button(window, text="Next Period", command=lambda: plot_and_move_next_period(fig, canvas,cb_var,), fg="dark green", bg = "white")
next_button.pack()
tk.Button(window, text="Quit", command=window.destroy, fg="dark green", bg = "white").pack() 

 
##for x in userchoice:
##     print("\nuser choice: " +str(x))

window.mainloop() #used to make the program work

# print ("econ value [" + str(econ()) + "]")


from results import display_results
display_results()


