import customtkinter
from PIL import ImageTk, Image
import io
from tkinter import filedialog
from tkinter import messagebox
import urllib.request
import tkinter as tk
import os
from pymem import Pymem

def load_image(url):
    raw_data = urllib.request.urlopen(url).read()
    im = Image.open(io.BytesIO(raw_data)).resize((25,25))
    image = ImageTk.PhotoImage(im)
    return image

path = ''
code = ''

customtkinter.set_appearance_mode('Light')
customtkinter.set_default_color_theme('blue')

def open_file():
    global path
    path = filedialog.askopenfilename(filetypes = [('File', '*.py *.txt'), ('All files', '*.*')])
    var1.set(0)
    var2.set(1)

def write_code():
    def dragonwin(event):
        x = window.winfo_pointerx() - window._offsetx
        y = window.winfo_pointery() - window._offsety
        window.geometry(f"+{x}+{y}")
    def clickonwin(event):
        window._offsetx = window.winfo_pointerx() - window.winfo_rootx()
        window._offsety = window.winfo_pointery() - window.winfo_rooty()
    def save():
        global code
        code = codebox.get(1.0, tk.END)
        window.destroy()
        var2.set(0)
        var1.set(1)
    window = customtkinter.CTk()
    window.title('Python Injector by maleh - Write code')
    window.overrideredirect(True)
    window._offsetx = 0
    window._offsety = 0
    window.resizable(False, False)
    window.geometry('1000x800')
    window.configure(background='#30a4cf')

    customtkinter.CTkLabel(master=window, text='Code:', text_font=('Consolas',13), text_color='white').place(y=10)
    customtkinter.CTkButton(master=window, text='Save & Close', text_font=('Consolas',11), text_color='white', command=save).place(x=845, y=10)
    codebox = tk.Text(master=window, font=('Consolas',11), width=120, height=150)
    codebox.pack(pady=50)

    window.bind('<Button-1>',clickonwin)
    window.bind('<B1-Motion>',dragonwin)
    window.mainloop()

def inject():
    process = process_entry.get()
    if process.strip() == '':
        messagebox.showerror('Error', message='You have to enter a process')
    else:
        if var1.get() == 1:
            global code
            try:
                pm = Pymem(process)
                pm.inject_python_interpreter()
                pm.inject_python_shellcode(code)
            except:
                messagebox.showerror(title='Error', message='There was an error:\n1. Maybe the process does not exist\n2. Maybe there was an error while injecting code')
        elif var2.get() == 1:
            global path
            if os.path.exists(path) and os.path.isfile(path):
                with open(path, 'r') as f:
                    code = f.read()
                    f.close()
                try:
                    pm = Pymem(process)
                    pm.inject_python_interpreter()
                    pm.inject_python_shellcode(code)
                except:
                    messagebox.showerror(title='Error', message='There was an error:\n1. Maybe the process does not exist\n2. Maybe there was an error while injecting code')
        else:
            messagebox.showerror(title='Error', message='You have to choose one option')

def change1():
    var2.set(0)
    var1.set(1)

def change2():
    var1.set(0)
    var2.set(1)

root = customtkinter.CTk()
root.title('Python Injector by maleh')
icon = load_image('https://cheatershome.netlify.app/icon_injector.ico')
root.call('wm', 'iconphoto', root._w, icon)
root.geometry('400x250')
root.resizable(False, False)
root.configure(background='#30a4cf')

var1 = customtkinter.IntVar()
var2 = customtkinter.IntVar()
var1.set(0)
var2.set(0)

customtkinter.CTkLabel(master=root, text='Process:', text_font=('Consolas',11), text_color='white').place(relx=.5, y=30, anchor=customtkinter.CENTER)
process_entry = customtkinter.CTkEntry(master=root, text_font=('Consolas',11), width=300)
process_entry.place(relx=.5, y=60, anchor=customtkinter.CENTER)
customtkinter.CTkLabel(master=root, text='Code:', text_font=('Consolas',11), text_color='white').place(relx=.5, y=100, anchor=customtkinter.CENTER)
customtkinter.CTkButton(master=root, text='Write code', text_font=('Consolas',11),text_color='white', cursor='hand2', command=write_code).place(relx=.3, y=140, anchor=customtkinter.CENTER)
customtkinter.CTkButton(master=root, text='Open file', text_font=('Consolas',11),text_color='white', cursor='hand2', command=open_file).place(relx=.7, y=140, anchor=customtkinter.CENTER)
check1 = customtkinter.CTkCheckBox(master=root, variable=var1, onvalue=1, offvalue=0, text='',text_font=('Consolas',9), text_color='white', command=change1).place(relx=.3, y=170, anchor=customtkinter.CENTER)
check1 = customtkinter.CTkCheckBox(master=root, variable=var2, onvalue=1, offvalue=0, text='',text_font=('Consolas',9), text_color='white', command=change2).place(relx=.7, y=170, anchor=customtkinter.CENTER)
customtkinter.CTkButton(master=root, text='Inject', text_font=('Consolas',15), text_color='white', cursor='hand2', command=inject).place(relx=.5, y=210, anchor=customtkinter.CENTER)
root.mainloop()
