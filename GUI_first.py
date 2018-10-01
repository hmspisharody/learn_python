import tkinter as tk
from tkinter import ttk

#window variable
win = tk.Tk()
win.title("HMS one")
win.resizable(0,0)

#Label creation
aLabel = ttk.Label(win, text = 'Enter your Name : ')
aLabel.grid(column=0, row=0)
numLabel = ttk.Label(win, text='Choose your age : ')
numLabel.grid(column=1, row=0)

#Button click subroutine
def clickMe():
  action.configure(text=name.get() + ' clicked Me!')
  aLabel.configure(text='Hi, ' + name.get(), foreground='red', background='blue')
  numLabel.configure(text = 'You are {} years old.'.format(number.get()), foreground='black', background='white')
  action.configure(state='disabled')

#button creation
action = ttk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=2, row=1)

#Entrybox(textbox) creation
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

#Combobox(Dropdownbox) creation
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = [i for i in range(18,80)]
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

#checkbuttons creation
ChkDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=ChkDis, state='disabled')
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

ChkUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unselected', variable=ChkUn)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

ChkEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=ChkEn)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

#Radiobutton creation
COLOR1 = 'Blue'
COLOR2 = 'Gold'
COLOR3 = 'Red'

def Rb_call():
  radSel = radVar.get()
  if radSel == 1: win.configure(background=COLOR1)
  if radSel == 2: win.configure(background=COLOR2)
  if radSel == 3: win.configure(background=COLOR3)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=Rb_call)
rad1.grid(column=0, row=5, sticky=tk.W)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=Rb_call)
rad2.grid(column=1, row=5, sticky=tk.W)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=Rb_call)
rad3.grid(column=2, row=5, sticky=tk.W)

nameEntered.focus()
win.mainloop()
