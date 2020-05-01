# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:19:02 2019

@author: bc130
"""

#######################
#imports
import tkinter as tk
from tkinter import ttk
#######################

############################ Create tkinkter instance
win = tk.Tk()
# Add title
win.title("Python GUI")
win.resizable(False,False)

# Add label
a_label = ttk.Label(win,text="Hello World").grid(column=0,row=0)

#Button event function
def click_me():
    action.configure(text="Yahoo You Clicked" + textbox.get())
    #a_label.configure(foreground='red')
    #a_label.configure(text='a red label')


##Add text box
textbox = tk.StringVar()
enteredtext = ttk.Entry(win , width = 12 , textvariable = textbox )
enteredtext.grid(column = 0 , row = 1)

##add button
action = ttk.Button(win,text="Click Me!",command = click_me)
action.grid(column=1,row=1)

##focus
enteredtext.focus()


### Combo Box
ttk.Label("")
######################
#Start GUI
win.mainloop()
#####################
