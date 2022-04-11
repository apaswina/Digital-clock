from tkinter import *

from time import strftime

def time():
    string=strftime('%I, %M, %S, %p')
    Label.config(text=string)
    Label.after(1000, time)

root=Tk()
root.title('Clock')
Label=Label(root, font=("Helvetica", 80), bg='black', fg='cyan')
Label.pack(anchor='center')

time()
