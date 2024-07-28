import tkinter as tk #for you it is pyqt5
from tkinter import * #MessageBox and Button
import tkinter.messagebox
import requests  #pip install requests
import os  #part of standard library
import sys  #part of standard library

VERSION = 2
link = "https://raw.githubusercontent.com/bluewolf44/united-GUI/main/version.txt"
check = requests.get(link)
print(check.text)
try:
    if float(VERSION) < float(check.text):
        print("help")
        filename = os.path.basename(sys.argv[0])

        for file in os.listdir():
            if file == filename:
                pass

            else:
                os.remove(file)

        exename = f'NameOfYourApp{float(check.text)}.exe'
        code = requests.get("https://raw.githubusercontent.com/bluewolf44/united-GUI/main/version.txt",
                            allow_redirects=True)
        open(exename, 'wb').write(code.content)

        root.destroy()
        os.remove(sys.argv[0])
        sys.exit()

except Exception as e:
    print(e)

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

canvas = tk.Canvas()
treeview = ttk.Treeview()

root.mainloop()