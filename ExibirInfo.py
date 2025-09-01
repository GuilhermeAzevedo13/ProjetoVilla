import customtkinter as ctk
from tkinter import Text, font
from Registro import *
from tkinter import *

class ExibirInfo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.todoExibirinfo()
        
    def layout_config(self):
        self.title("Exibir Mesas Cadastradas")
        self.geometry("600x300")
        self.resizable(False, False)
        
    def todoExibirinfo(self):
        fonte = font.Font(size=16, weight="bold")
        self.exibir = Text(self, font=fonte)
        self.exibir.pack(fill="both")
        
        registro = Registro()
        self.exibir.config(state=NORMAL)
        self.exibir.delete("1.0", END)
        self.exibir.insert("1.0", registro.ImprimirPessoa())
        self.exibir.config(state=DISABLED)
        
if __name__ == "__main__":
    exibir = ExibirInfo()
    exibir.mainloop()
