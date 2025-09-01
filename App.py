import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import ttk, font
from tkinter import messagebox
from Registro import *
from Morador import *
from RegistroMesas import RegistroMesasOcupadas
import pickle
from Mapa import Mapa
from ExibirInfo import ExibirInfo
from Buscar import Buscar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap("imagens\\icone.ico")
        self.layout_config()
        self.aparencia()
        self.todo_sistema()
        
    def layout_config(self):
        self.title("Reveillon Villa das Águas - Sistema de Cadastro de Mesa feito por " + "Guilherme Menezes de Azevedo©".upper())
        self.geometry("900x650")
        self.resizable(False, False)
        
    def aparencia(self):
        self.lb_apm = ctk.CTkLabel(self, text = "Tema", bg_color="transparent", text_color=['#000', '#fff']).place(x=50, y=430)
        self.opt_apm = ctk.CTkOptionMenu(self, values=["Dark", "Light", "System"], command=self.__change_apm).place(x=50, y= 460)

    def todo_sistema(self):
        # Crie variáveis StringVar para os campos de entrada
        # Inicialização de variáveis
        self.locatario_valor = StringVar()
        self.telefone_valor = StringVar()
        self.nome_valor = StringVar()
        self.endereco_valor = StringVar()
        self.comprovante_valor = StringVar()
        self.status_combobox = StringVar()
        self.mesa_combobox = StringVar()
        self.buscar_pessoa = StringVar()

        
        frame = ctk.CTkFrame(self, width = 700, height=50, corner_radius=0, bg_color="transparent", fg_color="transparent").place(x=0, y=10)
        title = ctk.CTkLabel(frame, text="REVEILLON VILLA DAS ÁGUAS", font=("Century Gothic bold", 24), text_color=['#000', '#fff'])
        title.pack(padx=20, pady=20)
        
        ordem = ctk.CTkLabel(self, text="Por favor, preencha todos os campos do formulário", font=("Century Gothic bold", 12), text_color=['#000','#fff']).place(x=50, y=70)

        
        # Entradas
        self.locatario_entry = ctk.CTkEntry(self, width=350, textvariable=self.locatario_valor, font=("Century Gothic bold", 16), fg_color="transparent")
        self.telefone_entry = ctk.CTkEntry(self, width=350, textvariable=self.telefone_valor, font=("Century Gothic bold", 16), fg_color="transparent")
        self.telefone_entry.bind("<Key>", self.__limitar_telefone_entry)
        self.nome_entry = ctk.CTkEntry(self, width=350, textvariable=self.nome_valor, font=("Century Gothic bold", 16), fg_color="transparent")
        self.endereco_entry = ctk.CTkEntry(self, width=350, textvariable=self.endereco_valor, font=("Century Gothic bold", 16), fg_color="transparent")
        self.comprovante_entry = ctk.CTkEntry(self, width=350, textvariable=self.comprovante_valor, font=("Century Gothic", 16), fg_color="transparent")
        self.mesa_entry = ctk.CTkEntry(self, width=350, textvariable=self.mesa_combobox, font=("Century Gothic bold", 16), fg_color="transparent")
        self.buscar_entry = ctk.CTkEntry(self, placeholder_text="Número da Mesa", placeholder_text_color="black", width=140, textvariable=self.buscar_pessoa, font=("Century Gothic bold", 16))

        #ComboBox
        self.status_pagamento = StringVar()
        self.status_combobox = ctk.CTkComboBox(self, values=["PAGO", "PENDENTE"], font=("Century Gothic bold", 14), state="readonly", variable=self.status_pagamento)
        self.status_combobox.set("PAGO")

        #Labels
        self.lb_nome_locatario = ctk.CTkLabel(self, text="Nome Completo do Locatário", font=("Century Gothic bold", 12), text_color=['#000','#fff'])
        self.lb_telefone = ctk.CTkLabel(self, text="Telefone do Locatário", font=("Century Gothic bold", 12), text_color=['#000','#fff'])
        self.lb_nome_proprietario = ctk.CTkLabel(self, text="Nome Completo do Proprietario", font=("Century Gothic bold", 12), text_color=['#000','#fff'])
        self.lb_endereco_completo = ctk.CTkLabel(self, text="Endereco Completo [Ex.: Qd 7, bl 3, ap 201 ou Quadra 10 , Lote 10]:", font=("Century Gothic bold", 12), text_color=['#000','#fff'])
        self.lb_comprovante = ctk.CTkLabel(self, text="Link do Comprovante", font=("Century Gothic bold", 12), text_color=['#000','#fff'])
        self.lb_status_pagamento = ctk.CTkLabel(self, text="Status do Pagamento", font=("Century Gothic bold", 12), text_color=['#000','#fff'])
        self.lb_mesa = ctk.CTkLabel(self, text="Mesas Disponíveis", font=("Century Gothic bold", 12), text_color=['#000','#fff'])
        
        # Adicione um ComboBox para seleção
        self.var = StringVar()
        self.lb_tipo_pessoa = ctk.CTkLabel(self, text="Escolha Abaixo entre MORADOR OU LOCATÁRIO", font=("Century Gothic bold", 12), text_color=['#000','#fff'])
        self.lb_tipo_pessoa.place(x= 450, y= 120)
        self.tipo_pessoa_combobox = ctk.CTkComboBox(self, values=["MORADOR", "LOCATARIO"], font=("Century Gothic bold", 14), state="readonly", variable=self.var, command=self.__atualizar)
        self.tipo_pessoa_combobox.set("MORADOR")
        self.tipo_pessoa_combobox.place(x=450, y=150)
        
    
                
        self.lb_nome_proprietario.place(x=50, y=120)
        self.nome_entry.place(x=50, y=150)

        self.lb_endereco_completo.place(x=50, y=180)
        self.endereco_entry.place(x=50, y=210)

        self.lb_comprovante.place(x=50, y=240)
        self.comprovante_entry.place(x=50, y=270)

        self.lb_status_pagamento.place(x=50, y=300)
        self.status_combobox.place(x=50, y=330)
        
        self.lb_mesa.place(x=50, y=360)
        
        self.mesa_combobox = ttk.Combobox(self, font=("Century Gothic bold", 12), state="readonly")
        self.mesa_combobox.place(x=50, y=390)
        self.__atualizar_combobox_mesas()

        
        self.buscar_entry.place(x=260, y=570)


        #Botoes
        botao_SalvarRegistro = ctk.CTkButton(self, text="SALVAR DADOS".upper(), command=self.__inserir, fg_color="#151", hover_color="#131")
        botao_SalvarRegistro.place(x=260, y=430)

        botao_limparCampos = ctk.CTkButton(self, text="LIMPAR CAMPOS".upper(), command = self.__limpar, fg_color="#555", hover_color="#333")
        botao_limparCampos.place(x=420,y=430)
        botao_mapa = ctk.CTkButton(self, text="MAPA".upper(), command = self.__mapa, fg_color="#151", hover_color="#131").place(x=260,y=480)
        botao_buscar_pessoa = ctk.CTkButton(self, text="Buscar Mesa".upper(), command = self.__buscar, fg_color="#151", hover_color="#131").place(x = 260, y = 530)
        botao_exibir_info = ctk.CTkButton(self, text="exibir informações".upper(), command=self.__exibirInfo, fg_color="#555", hover_color="#333")
        botao_exibir_info.place(x = 420, y = 480)
        botao_remover_pessoa = ctk.CTkButton(self, text="remover mesa".upper(), command=self.__remover, fg_color="#555", hover_color="#333")
        botao_remover_pessoa.place(x = 420, y = 530)
        botao_alterar_Status = ctk.CTkButton(self, text="alterar status".upper(), command=self.__alterar_status, fg_color="#555", hover_color="#333")
        botao_alterar_Status.place(x = 420, y = 570)
    
    def __inserir(self):
        tentativas = 0
        morador = None
        locatario = None
        while tentativas < 3:
            try:
                # Get data from entry fields
                locatario = self.locatario_valor.get()   
                telefone = self.telefone_valor.get()
                nome = self.nome_valor.get()
                endereco = self.endereco_valor.get()
                comprovante = self.comprovante_valor.get()
                status = self.status_combobox.get()
                mesa = self.mesa_combobox.get()
                # converter tudo para maiusculo
                locatario = locatario.upper()
                nome = nome.upper()
                endereco = endereco.upper()
                status = status.upper()

                registro = Registro()
                registroMesa = RegistroMesasOcupadas()

                if self.var.get() == "MORADOR":
                    try:
                        morador = Morador(nome, endereco, comprovante, status, mesa)
                    except ValueError as error:
                        tentativas += 1
                        if tentativas < 3:
                            messagebox.showerror("Sistema", f"Tentativa: {tentativas}: Erro - {error}")
                    registro.InserirPessoa(morador)
                    registroMesa.InserirMesaOcupada(mesa)
                    messagebox.showinfo("Sistema", "Morador inserido com sucesso!")

                elif self.var.get() == "LOCATARIO":
                    locatario_exists = False
                    for pessoa in registro.get_registro():
                        if isinstance(pessoa, Locatario) and pessoa.get_nome_locatario() == locatario:
                            locatario_exists = True
                            break
                    if locatario_exists:
                        messagebox.showinfo("Sistema", "Nome do Locatário já existe.")
                        return
                    try:
                        locatario = Locatario(nome, endereco, comprovante, status, mesa, locatario, telefone)
                    except ValueError as error:
                        tentativas += 1
                        if tentativas < 3:
                            messagebox.showerror("Sistema", f"Tentativa: {tentativas}: Erro - {error}")
                        else:
                            messagebox.showerror("Sistema", f"Número máximo de tentativas excedido. Volte ao menu principal.")
                    registro.InserirPessoa(locatario)
                    registroMesa.InserirMesaOcupada(mesa)
                    messagebox.showinfo("Sistema", "Locatário inserido com sucesso")
                break
            except ValueError as error:
                tentativas += 1
                if tentativas < 3:
                    messagebox.showerror("Sistema", f"Tentativa {tentativas}: Erro - {error}")
                else:
                    messagebox.showerror("Sistema", f"Número máximo de tentativas excedido. Volte ao menu principal.")
        self.__atualizar_combobox_mesas()


    def __atualizar_combobox_mesas(self):
        filename = 'registroMesas.dat'
        # Verifique se o arquivo existe
        if os.path.exists(filename):
            # Se o arquivo existir, leia a lista de mesas ocupadas
            with open(filename, 'rb') as file:
                mesas_ocupadas = pickle.load(file)
        else:
            # Se o arquivo não existir, crie-o e inicialize-o com uma lista vazia
            mesas_ocupadas = []
            with open(filename, 'wb') as file:
                pickle.dump(mesas_ocupadas, file)
                
        # Converte as mesas ocupadas em uma lista de inteiros
        mesas_ocupadas = [int(mesa) for mesa in mesas_ocupadas]
        # Atualize o Combobox com as mesas disponíveis
        mesas_disponiveis = [int(i) for i in range(1, 101) if i not in mesas_ocupadas]
        
        # Certifique-se de que o Combobox não esteja vazio antes de definir o valor
        if mesas_disponiveis:
            self.mesa_combobox['values'] = mesas_disponiveis
            self.mesa_combobox.set(mesas_disponiveis[0])
        else:
            self.mesa_combobox.set("")  # Ou defina para um valor padrão se preferir

    def __atualizar(self, variavel):
        
        variavel = self.tipo_pessoa_combobox.get()
        
        if variavel == "LOCATARIO":
            
            self.lb_nome_locatario.place(x=450, y=180)
            self.locatario_entry.place(x=450, y=210)

            self.lb_telefone.place(x=450, y=240)
            self.telefone_entry.place(x=450, y=270)
            
        if variavel == "MORADOR":
            self.lb_nome_locatario.place_forget()
            self.locatario_entry.place_forget()

            self.lb_telefone.place_forget()
            self.telefone_entry.place_forget()
            
    def __limitar_telefone_entry(self, event):
        telefone = self.telefone_valor.get()
        if len(telefone) >= 11:
            self.telefone_entry.delete(10, "end")  # Limita a entrada a 11 dígitos
        
        
    def __exibirInfo(self):
        abrirExibirInfo = ExibirInfo()
        abrirExibirInfo.mainloop()
        
    def __remover(self):
        self.remover_mesa = StringVar()
        self.janelaExibir2 = Toplevel()
        self.janelaExibir2.geometry("300x100")
        self.janelaExibir2.resizable(False, False)
        self.janelaExibir2.title("Remover Mesa Cadastrada".upper())
        
        fonte2 = font.Font(size=16, font="Arial", weight="bold")
        self.label_remover = tk.Label(self.janelaExibir2, text="Número da mesa a ser removida:", font=fonte2)
        self.label_remover.pack()
        self.remover_mesa = tk.Entry(self.janelaExibir2)
        self.remover_mesa.pack()
        botao_remover_pessoa = tk.Button(self.janelaExibir2, text="Remover Mesa", command=self.__funcao_para_remover)
        botao_remover_pessoa.pack()
        
    def __funcao_para_remover(self):
        numero_da_mesa = self.remover_mesa.get()
        registro1 = Registro()
        registro2 = RegistroMesasOcupadas()
        try:
            registro1.RemoverPessoaPorMesa(numero_da_mesa)
            registro2.RemoverMesaOcupada(numero_da_mesa)
        except ValueError as error:
            messagebox.showinfo("Sistema", f"Erro - {error}")
        else:
            messagebox.showinfo("Sistema", f"Mesa {numero_da_mesa} removida com sucesso.")
            self.__atualizar_combobox_mesas()
            self.janelaExibir2.destroy()

    def __change_apm(self, nova_aparencia):
        ctk.set_appearance_mode(nova_aparencia)
        
    
    def __limpar(self):
        self.locatario_valor.set("")
        self.telefone_valor.set("")
        self.nome_valor.set("")
        self.endereco_valor.set("")
        self.comprovante_valor.set("")
        self.buscar_pessoa.set("")
        
    def __mapa(self):
        abrirMapa = Mapa()
        abrirMapa.mainloop()
    
    def __buscar(self):
        filename = 'registroMesas.dat'
        # Verifique se o arquivo existe
        if os.path.exists(filename):
            # Se o arquivo existir, leia a lista de mesas ocupadas
            with open(filename, 'rb') as file:
                mesas_ocupadas = pickle.load(file)
        # Converte as mesas ocupadas em uma lista de inteiros
        mesas_ocupadas = [int(mesa) for mesa in mesas_ocupadas]
                
        mesa = self.buscar_pessoa.get()
    
        if not mesa:
            messagebox.showinfo("Sistema", "Insira um número de mesa válido.")
            return
        
        # Verifique se a mesa é maior do que a quantidade máxima de mesas (neste caso, 100)
        if int(mesa) < 1 or int(mesa) > 100:
            messagebox.showinfo("Sistema", "Mesa não existe.")
        elif int(mesa) in mesas_ocupadas:
            abrirBuscar = Buscar(mesa)
            abrirBuscar.mainloop()
        else:
            messagebox.showinfo("Sistema", "Mesa Desocupada")
            
    def __alterar_status(self):
        self.janela_alterar_status = Toplevel()
        self.janela_alterar_status.title("Alterar Status")
        self.janela_alterar_status.geometry("300x200")
        
        label_mesa = ctk.CTkLabel(self.janela_alterar_status, text="Número da Mesa:", font=("Century Gothic bold", 12), text_color="#000000")
        label_mesa.pack(pady=10)
        
        mesa_entry = ctk.CTkEntry(self.janela_alterar_status, width=50)
        mesa_entry.pack()
        
        label_novo_status = ctk.CTkLabel(self.janela_alterar_status, text="Novo Status:", font=("Century Gothic bold", 12), text_color="#000000")
        label_novo_status.pack(pady=10)
        
        novo_status_combobox = ctk.CTkComboBox(self.janela_alterar_status, values=["PAGO", "PENDENTE"], font=("Century Gothic bold", 12), state="readonly")
        novo_status_combobox.pack()
        novo_status_combobox.set("PAGO")
        
        botao_confirmar = ctk.CTkButton(self.janela_alterar_status, text="Confirmar", command=lambda: self.__confirmar_alteracao_status(mesa_entry.get(), novo_status_combobox.get()))
        botao_confirmar.pack(pady=10)
        
    def __confirmar_alteracao_status(self, mesa, novo_status):
        # Verifique se a mesa está ocupada
        registro = Registro()
        status_atual = registro.ObterStatusPorMesa(mesa)
        
        if status_atual is not None:
            if status_atual == novo_status:
                messagebox.showinfo("Sistema", "O status não foi alterado.")
            else:
                registro.AtualizarStatusPorMesa(mesa, novo_status)
                messagebox.showinfo("Sistema", f"O status da mesa {mesa} foi alterado para {novo_status}.")
                self.__atualizar_combobox_mesas()
            self.janela_alterar_status.destroy()
        else:
            messagebox.showinfo("Sistema", "Mesa não encontrada ou está desocupada.")
            
    def __alterar_comprovante(self):
        pass        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()