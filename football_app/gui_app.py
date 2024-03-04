from tkinter import *
from tkinter import ttk

def get_data():
    value = entry.get()
    print("You entered :", value)


root = Tk()
style = ttk.Style()
style.configure('Red.TButton', foreground='red', font = ('Calibri',10,'bold'))

frm = ttk.Frame(root, padding=15)
frm.grid()
ttk.Label(frm,text="Wprowadź nazwę:").grid(column=0, row=0)
ttk.Button(frm,text="Generuj wykres", command = get_data()).grid(column=3, row=0)
ttk.Button(frm, text="Quit", command=root.destroy, style='Red.TButton').grid(column=5, row=1)
entry=ttk.Entry(frm).grid(column=2, row=0)
root.mainloop()