import customtkinter as ctk
from tkinter import messagebox
from Registro import *
from tkinter import *
import tkinter as tk

class Buscar(ctk.CTk):
    def __init__(self, mesa):
        super().__init__()
        self.layout_config()
        self.todoBuscar(mesa)
        
    def layout_config(self):
        self.title("Informações da Pessoa")
        self.geometry("450x250")
        self.resizable(False, False)
        
    def todoBuscar(self, mesa):
        registro = Registro()
        resultados_da_busca = registro.PesquisarMesa(mesa)
    
        if resultados_da_busca is not None:
            if isinstance(resultados_da_busca, Morador):
                # Encontrou a pessoa na mesa, exiba as informações
                self.__exibir_informacoes(resultados_da_busca)
        else:
            print("Classe Buscar da Mesa nao Encontrada")
            messagebox.showinfo("Sistema", f"Mesa {mesa} está desocupada.")
        
    def __exibir_informacoes(self, dados_pessoa):
        # Crie widgets na nova janela para exibir as informações em comum
        if isinstance(dados_pessoa, Morador):
            nome = ctk.CTkLabel(self, text="Nome: " + dados_pessoa.get_nome(), font=("Century Gothic bold", 16), text_color=['#000', '#fff'])
            nome.place(x=0,y=10)
            endereco = ctk.CTkLabel(self, text="Endereço: " + dados_pessoa.get_endereco(), font=("Century Gothic bold", 16), text_color=['#000', '#fff'])
            endereco.place(x=0,y=35)
            comprovante2 = ctk.CTkLabel(self, text="Comprovante:", font=("Century Gothic bold", 16), text_color=['#000', '#fff'])
            comprovante2.place(x=0,y=60)
            # Crie um Entry para o campo "Comprovante"
            comprovante = tk.Entry(self)
            comprovante.insert(0, dados_pessoa.get_comprovante())
            comprovante.config(state="readonly")
            comprovante.place(x=100, y=65)
            status = ctk.CTkLabel(self, text="Status de Pagamento: " + dados_pessoa.get_statuspagamento(), font=("Century Gothic bold", 16), text_color=['#000', '#fff'])
            status.place(x=0,y=85)
            mesa = ctk.CTkLabel(self, text="Mesa: " + str(dados_pessoa.get_mesa()), font=("Century Gothic bold", 16), text_color=['#000', '#fff'])
            mesa.place(x=0,y=110)

        if isinstance(dados_pessoa, Locatario):
            # Para Locatario, exiba informações adicionais (nome_locatario e telefonelocatario)
            nome_locatario = ctk.CTkLabel(self, text="Nome do Locatário: " + dados_pessoa.get_nome_locatario(), font=("Century Gothic bold", 16), text_color=['#000', '#fff'])
            nome_locatario.place(x=0,y=135)
            telefone_locatario = ctk.CTkLabel(self, text="Telefone do Locatário: " + dados_pessoa.get_telefonelocatario(), font=("Century Gothic bold", 16), text_color=['#000', '#fff'])
            telefone_locatario.place(x=0,y=160)
        
if __name__ == "__main__":
    buscar = Buscar()
    buscar.mainloop()