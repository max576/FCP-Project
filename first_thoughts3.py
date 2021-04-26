  # -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:02:31 2021

@author: User

MAIN PURPOSE AND ACTIONS DESCRIBED HERE



"""
##bitvalues
FACEMASKS = 1
DISTANCING = 2
LOCKDOWN = 4
BORDERS = 8
PUBS = 16
NON_ESSENTIAL = 32 

INVALID_ENTRY = 0

class epidemic_control:
    def __init__(self, controlid,name, prompt, bitvalue, weight):
        # Basic simulation parameters:
        self.controlid = controlid
        self.name = name
        self.prompt = prompt
        self.bitvalue = bitvalue
        self.weight = weight

        
def importControls(controls):
    
    ###TODO - provide csv import option for control list parameters
    
    controls.append(epidemic_control(0,"Distancing","Enter [Y] to implement 2 metre social distancing rules, [N] to ignore this measure : ",DISTANCING,[20,40,5,20,30,40]))
    controls.append(epidemic_control(1,"Facemask","Enter [Y] to implement facemasks, [N] to ignore this measure : ",FACEMASKS,[15,25,75,34,56,90]))
    controls.append(epidemic_control(2,"Pubs","Enter [Y] to implement pubs early closing, [N] to ignore this measure : " ,PUBS,[20,40,5,20,30,40]))
    controls.append(epidemic_control(3,"Non-Essential","Enter [Y] to close non-essential shops, [N] to ignore this measure : ",NON_ESSENTIAL,[20,40,5,20,30,40]))
    controls.append(epidemic_control(4,"Borders","Enter [Y] to close international borders, [N] to ignore this measure : ",BORDERS,[20,40,5,100,30,40]))
    controls.append(epidemic_control(5,"Lockdown","Enter [Y] to implement a full National Lockdown, [N] to ignore this measure : ",LOCKDOWN,[20,40,5,20,30,40]))
    

        
def user_input(controls):
    allowedChars = "YNQ"
    i = 0
    userchoice = INVALID_ENTRY
    while i != len(controls):
        #print(controls[i].name)y
        
        mode = input(controls[i].prompt).upper()
        while (len(mode) != 1 or mode not in allowedChars):
            print("DON'T BE A MELT, THIS IS NOT A DRILL!")
            mode = input(controls[i].prompt).upper()
        if mode == "Y" : userchoice = userchoice + controls[i].bitvalue
        i += 1
        if mode == "Q" : 
            userchoice = INVALID_ENTRY
            break
    return userchoice
          

"""
MAIN PROCESSING LOOP
"""
while True:
    ctl = []   
    userchoice = []
    importControls(ctl)
        
    #p = periodic cycles of the simulation
    for p in range(6):

        print("**************************************************")
        print("*      A T T E M P T " + str(p) + "      *")
        print("**************************************************")
        userchoice.append(user_input(ctl))
        if userchoice[p] == 0 : break
    
        #PART 2    
        ###analyse
        
        ##PART 3 
            ###Generate Graphs
            
        print("**************************************************")
        print("*       Y O U   H A V E   S E L E C T E D        *")
        print("**************************************************")
        print("\n(bitwise value) : " + str(userchoice))
    
        i=0
        while i != len(ctl):      
            #print("\nlen control : " + str(len(ctl)))
            #print("\nuserchoice : " + str(userchoice))
            #print("\nbitvalue: " + str(ctl[i].bitvalue))
            #print("\ni: " + str(i))         
            #print("\nbit: " + str(userchoice & ctl[i].bitvalue))  
       
            #print("\np: " + str(p))
            #print("\nweight cycle 3: " + str(ctl[i].weight[p]))     
            if (userchoice[p] & ctl[i].bitvalue) != 0 : print (ctl[i].name + " : " + str(ctl[i].bitvalue) ) 
            i += 1
     
    break
        
for x in userchoice:
      print("\nuser choice: " +str(x))
 
print("***********************************")
print("*            Bye Bye              *")
print("*                                 *")
print("*    Thank you for taking part    *")
print("*                                 *")
print("*     Press F5 to play again      *")
print("***********************************")



