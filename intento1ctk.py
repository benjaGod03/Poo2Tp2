import tkinter as tk
from tkinter import ttk
from customtkinter import CTk, CTkToplevel, CTkComboBox, CTkFrame, CTkLabel, CTkEntry, CTkButton
import main1 as pg


class Window:
    def __init__(self):
        self.app = CTk()
        self.app.geometry("800x600")

        ttk.Label(self.app, text="Grafos",  
                  background='grey', foreground="light blue",  
                  font=("Times New Roman", 20), anchor='center').grid(row=0, column=1)
        ttk.Label(self.app, text="Seleccione el Grafo :", 
                  font=("Times New Roman", 15)).grid(column=0, 
                  row=5, padx=10, pady=25)

        self.combobox = CTkComboBox(master=self.app, values=["Grafo 1", "Grafo 2"], fg_color="#0093E9", 
                                     border_color="#FBAB7E", dropdown_fg_color="#0093E9", command=self.opciones)
        self.combobox.place(relx=0.5, rely=0.5, anchor="center") 

        self.app.mainloop()

    def opciones(self, value):
        if value == "Grafo 1":
            g1 = CTkToplevel()
            g1.geometry("600x400")
            g1.title("Grafo 1")
            frame_entrada = CTkFrame(g1)  
            frame_entrada.pack(pady=20, padx=20, fill="both", expand=True)
            label_nombre1 = CTkLabel(frame_entrada, text="Introduce un nombre:")
            label_nombre1.pack(pady=5)
            entry_nombre1 = CTkEntry(frame_entrada, width=200)
            entry_nombre1.pack(pady=5)
            label_nombre2 = CTkLabel(frame_entrada, text="Introduce otro nombre:") 
            label_nombre2.pack(pady=5)
            entry_nombre2 = CTkEntry(frame_entrada, width=200)
            entry_nombre2.pack(pady=5)
            button_calcular = CTkButton(frame_entrada, text="Calcular distancia", command=pg.calcular_distancia)
            button_calcular.pack(pady=10)   
            label_resultado = CTkLabel(frame_entrada, text="") 
            label_resultado.pack(pady=10)
            frame_grafo = CTkFrame(g1)
            frame_grafo.pack(pady=20, padx=20, fill="both", expand=True)
        else:
            print("bb")

if __name__ == "__main__":
    window = Window()