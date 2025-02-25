import customtkinter as c
import tkinter as tk
import tkinter.messagebox as mbox
import tkinter.filedialog as fdiag
import tkinter.dialog as d

class GUI():
    def InitGUI():
        window = tk.Tk(screenName="MP3ToOGG", baseName="MP3ToOGG")
        textm = tk.Label(text="This is My First Program for Converting MP3 to OGG format... So Enjoy to use this!!!", foreground="#003e94")
        entry = tk.Entry()
        window.geometry("600x920")
        but = tk.Button(text="Convert!!!", command=lambda : print(entry.get()))
        entry.pack()
        but.pack()
        textm.pack()
        window.mainloop()