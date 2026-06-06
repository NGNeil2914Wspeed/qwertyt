import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Hello")

mainframe = tk.Frame(root, width=100, height=100, bg="yellow")
mainframe.pack()

tk.Button(mainframe, text="1").grid(row=1, column=1, padx=20, pady=20)
tk.Button(mainframe, text="2").grid(row=1, column=2, padx=20, pady=20)
tk.Button(mainframe, text="3").grid(row=1, column=3, padx=20, pady=20)

tk.Button(mainframe, text="4").grid(row=2, column=1, padx=20, pady=20)
tk.Button(mainframe, text="5").grid(row=2, column=2, padx=20, pady=20)
tk.Button(mainframe, text="6").grid(row=2, column=3, padx=20, pady=20)

tk.Button(mainframe, text="7").grid(row=3, column=1, padx=20, pady=20)
tk.Button(mainframe, text="8").grid(row=3, column=2, padx=20, pady=20)
tk.Button(mainframe, text="9").grid(row=3, column=3, padx=20, pady=20)

root.mainloop()