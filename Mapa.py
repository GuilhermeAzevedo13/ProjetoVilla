import customtkinter as ctk
from tkinter import *
from Buscar import Buscar
from tkinter import messagebox, PhotoImage
from Registro import Registro
import os

class Mapa(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.todo_mapa()
        
        
    def layout_config(self):
        self.title("Mapa das Mesas - Sistema de Cadastro de Mesa feito por " + "Guilherme Menezes de Azevedo©".upper())
        self.geometry("1000x650")
        self.resizable(False, False)
        
    def __abrir_detalhes_mesa(self, mesa_numero):
        mesa = str(mesa_numero)
        if not mesa:
            messagebox.showinfo("Sistema", "Insira um número de mesa válido.")
            return
        registro = Registro()
        mesa_encontrada = registro.PesquisarMesa(mesa)
        if mesa_encontrada is not None:
            abrirBuscar = Buscar(mesa)
            abrirBuscar.mainloop()
        else:
            messagebox.showinfo("Sistema", f"Mesa {mesa} não encontrada")


    
    def criar_canvas_mesa(self, mesa_numero, x, y):
        registro = Registro()
        status = registro.ObterStatusPorMesa(str(mesa_numero))
        
        if status == "PAGO":
            cor = "red"
        elif status == "PENDENTE":
            cor = "yellow"
        elif status is None:
            cor = "white"
        else:
            cor = "gray"

        canvas_mesa = Canvas(self, width=30, height=29, bg=cor)
        canvas_mesa.place(x=x, y=y)
        
        def __passando_por_cima(event):
            canvas_mesa.configure(bg="#C0C0C0")
            
        def __tirando_de_cima(event):
            canvas_mesa.configure(bg=cor)
            
        canvas_mesa.bind("<Enter>", __passando_por_cima)
        canvas_mesa.bind("<Leave>", __tirando_de_cima)
        canvas_mesa.bind("<Button-1>", lambda event, num=mesa_numero: self.__abrir_detalhes_mesa(num))
        
        # Adicione o número da mesa como um Text widget no Canvas
        canvas_mesa.create_text(15, 15, text=str(mesa_numero), font=("Century Gothic bold", 10), fill="#000000")
        
    def todo_mapa(self):
        # Calcula as coordenadas para o retângulo verde no centro
        largura_retangulo = 900
        altura_retangulo = 600
        x_retangulo = (self.winfo_width() - largura_retangulo) / 2
        y_retangulo = (self.winfo_height() - altura_retangulo) / 2

        # Cria o retângulo verde
        retangulo = ctk.CTkFrame(self, width=largura_retangulo, height=altura_retangulo, bg_color="green", fg_color="transparent")
        retangulo.place(x=x_retangulo, y=y_retangulo)
        
        # Substitua a criação do retângulo verde
        
        imagem = PhotoImage(file="imagens\\fotoMapa.png", master=self)
        imagem_label = Label(retangulo, image=imagem, borderwidth=0)
        imagem_label.photo = imagem  # Isso evita que a imagem seja coletada pelo coletor de lixo
        imagem_label.place(x=0, y=0)

        # Certifique-se de que o tamanho da label seja o mesmo que o da imagem
        imagem_label.configure(width=largura_retangulo, height=altura_retangulo)
        
        brinquedos = ctk.CTkFrame(self, width = 150, height=150, corner_radius=0, bg_color="#1E90FF", fg_color="transparent")
        brinquedos.place(x=755, y=460)
        
        imagem2 = PhotoImage(file="imagens\\brinquedos.png", master=self)
        imagem_label2 = Label(brinquedos, image=imagem2, borderwidth=0)
        imagem_label2.photo = imagem2
        imagem_label2.place(x=0,y=0)
        imagem_label2.config(width=150, height=150)
        
        palco = ctk.CTkFrame(self, width = 200, height=180, corner_radius=0, bg_color="#A9A9A9", fg_color="transparent")
        palco.place(x = 50, y = 225)
        imagem3 = PhotoImage(file="imagens\\palco.png", master=self)
        imagem_label3 = Label(palco, image=imagem3, borderwidth=0)
        imagem_label3.photo = imagem3
        imagem_label3.place(x=0,y=0)
        imagem_label3.config(width=200, height=180)
        
        casinha = brinquedos = ctk.CTkFrame(self, width = 150, height=150, corner_radius=0, bg_color="#A9A9A9", fg_color="transparent")
        casinha.place(x = 80, y = 460)
        imagem4 = PhotoImage(file="imagens\\casinha.png", master=self)
        imagem_label4 = Label(casinha, image=imagem4, borderwidth=0)
        imagem_label4.photo = imagem4
        imagem_label4.place(x=0,y=0)
        imagem_label4.config(width=150, height=150)
        
        entrada = brinquedos = ctk.CTkFrame(self, width = 70, height=45, corner_radius=0, bg_color="white", fg_color="transparent")
        entrada.place(x = 120, y = 580)
        label_casinha = ctk.CTkLabel(self, text="entrada".upper(), font=("Century Gothic bold", 10), text_color="#fff")
        label_casinha.place(x=130,y=590)
        
        # Botoes no Setor Oeste
        x_mesa, y_mesa = 260, 460  # Coordenadas do primeiro botão de mesa
        espacamento_x = 45  # Espaçamento horizontal entre botões de mesa
        espacamento_y = 60  # Espaçamento vertical entre botões de mesa
        mesas_por_coluna = 10  # Número de mesas por coluna
        mesas_por_linha = 3  # Número de mesas por linha

        for mesa_numero in range(1, 31):
            self.criar_canvas_mesa(mesa_numero, x_mesa, y_mesa)
            x_mesa += espacamento_x

            if mesa_numero % mesas_por_coluna == 0:
                x_mesa = 260
                y_mesa += espacamento_y
        mesa_numero = str(mesa_numero)
        
        # Botoes no Setor Leste
        x_mesa, y_mesa = 260, 45  # Coordenadas do primeiro botão de mesa
        espacamento_x = 45  # Espaçamento horizontal entre botões de mesa
        espacamento_y = 60  # Espaçamento vertical entre botões de mesa
        mesas_por_coluna = 10  # Número de mesas por coluna
        mesas_por_linha = 3  # Número de mesas por linha

        for mesa_numero in range(31, 61):
            self.criar_canvas_mesa(mesa_numero, x_mesa, y_mesa)
            x_mesa += espacamento_x

            if mesa_numero % mesas_por_coluna == 0:
                x_mesa = 260
                y_mesa += espacamento_y
        mesa_numero = str(mesa_numero)
                
        # Botoes no Setor Sul
        x_mesa, y_mesa = 720, 45  # Coordenadas do primeiro botão de mesa
        espacamento_x = 45  # Espaçamento horizontal entre botões de mesa
        espacamento_y = 53  # Espaçamento vertical entre botões de mesa
        mesas_por_coluna = 5  # Número de mesas por coluna

        for mesa_numero in range(61, 101):
            self.criar_canvas_mesa(mesa_numero, x_mesa, y_mesa)
            x_mesa += espacamento_x

            if mesa_numero % mesas_por_coluna == 0:
                x_mesa = 720  # Resetar x_mesa para çomeçar em outra coluna
                y_mesa += espacamento_y
        mesa_numero = str(mesa_numero)
        
if __name__ == "__main__":
    mapa = Mapa()
    mapa.mainloop()