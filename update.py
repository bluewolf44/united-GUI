"""A demo script to showcase the Sun Valley ttk theme."""

import tkinter
from tkinter import ttk

import sv_ttk
import requests
import os
import sys


current_version = 0.1
link = "https://raw.githubusercontent.com/bluewolf44/united-GUI/main/version.txt"

class Update(ttk.LabelFrame):
    def __init__(self, parent,version):
        super().__init__(parent, padding=10,text="Do you want to update to "+version)

        self.update = ttk.Button(self,text="Update")
        self.update.grid(row = 0,column=0,padx=25,pady=10)

        self.dont = ttk.Button(self,text="Skip")
        self.dont.grid(row = 0,column=1,padx=25,pady=10)



def update():
    check = requests.get(link)
    if float(current_version) < float(check.text):
        filename = os.path.basename(sys.argv[0])
        print(os.listdir())


    root = tkinter.Tk()
    root.title("")

    sv_ttk.set_theme("dark")

    Update(root,"0.100").pack(expand=False,padx=10,pady=10)
    ttk.Label(root,text = "Current version:" + str(current_version),padding=5).pack(anchor="w")
    root.resizable(False, False)

    root.mainloop()