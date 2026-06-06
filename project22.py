import tkinter as tk
from tkinter import END, DISABLED

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Hello")

current_step = 1

mainframe = tk.Frame(root, height=500, width=500)
mainframe.pack(pady=50)

name_label = tk.Label(mainframe, text="Please enter your name:")
name_label.pack()

name_entry = tk.Entry(mainframe)
name_entry.pack()

last_name_label = tk.Label(mainframe, text="Please enter your last name: ")
last_name_label.pack()

last_name_entry = tk.Entry(mainframe)
last_name_entry.pack()

def switch():
    global current_step
    
    val1 = name_entry.get().strip()
    val2 = last_name_entry.get().strip()
    
    if not val1 or not val2:
        return

    if current_step == 1:
        name_label.config(text="Enter your gmail")
        last_name_label.config(text="Enter your password")
        
        name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        
        current_step = 2
    elif current_step == 2:
        end()

def end():
    name_label.pack_forget()
    name_entry.pack_forget()
    last_name_entry.pack_forget()
    next_button.pack_forget()
    
    last_name_label.config(text="Congratulations, your account is made!")

next_button = tk.Button(mainframe, command=switch, text="Next")
next_button.pack(pady=10)

root.mainloop()
