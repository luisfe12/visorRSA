from tkinter import *
from tkinter import filedialog
import anali_rsa
import tkinter as tk

ventana = tk.Tk()
ventana.title("analisis PEM")
ventana.geometry("500x500")

#leemos ventana
ventana.filename = filedialog.askopenfilename(initialdir="/PYTHONPR/rsa_python", title="Selecciona los PEM", filetypes=(("arc pem", "*.pem"), ("all files", "*.*")))

scrollbar = tk.Scrollbar(ventana)
#creamos camvas para entrar frames
c=tk.Canvas(ventana, yscrollcommand=scrollbar.set)
scrollbar.config(command = c.yview)
scrollbar.pack(side = tk.RIGHT, fill=tk.Y)
elframe = tk.Frame(c)
c.pack(side="left", fill="both", expand=True)
c.create_window(0,0,window=elframe,anchor='nw')

#obtenmos ruta
dato_rsa = anali_rsa.analizar(ventana.filename)
my_direccion = Label(elframe,wraplength=1500, text = dato_rsa).pack()
# my_direccion = Label(ventana, text = ventana.filename).pack()
# my_direccion = Label(ventana, text = ventana.filename).pack()
# my_direccion = Label(ventana, text = ventana.filename).pack()
# my_direccion = Label(ventana, text = ventana.filename).pack()
# my_direccion = Label(ventana, text = ventana.filename).pack()#si lo repetimos sale bien
print(ventana.filename)
ventana.update()
c.config(scrollregion=c.bbox("all"))
ventana.mainloop()
