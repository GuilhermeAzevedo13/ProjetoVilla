import pickle
import os
from Morador import Morador
from Locatario import Locatario

class Registro:
    def __init__(self, arquivo='registro.dat'):
        self.__registrarMorador = []
        self.__arquivo = arquivo

        if not os.path.exists(self.__arquivo):
            with open(self.__arquivo, 'wb'):
                pass  # Cria um arquivo vazio

        try:
            with open(self.__arquivo, 'rb') as file:
                self.__registrarMorador = pickle.load(file)
        except (FileNotFoundError, EOFError):
            pass

    def get_registro(self):
        return self.__registrarMorador
    
    def InserirPessoa(self, morador):
        if not isinstance(morador, (Morador, Locatario)):
            raise ValueError("Insira um morador ou locatário válido!")

        mesa = morador.get_mesa()
        for pessoa in self.__registrarMorador:
            if isinstance(pessoa, (Morador, Locatario)) and pessoa.get_mesa() == mesa:
                raise ValueError("Já existe uma pessoa na mesa selecionada no Registro")
        if isinstance(morador, (Morador, Locatario)):
            nome = morador.get_nome()
            for pessoa in self.__registrarMorador:
                if isinstance(pessoa, (Morador)) and pessoa.get_nome() == nome:
                    raise ValueError("Já existe uma Pessoa com esse nome no Registro")

        self.__registrarMorador.append(morador)
        self.__salvar_registro()
        

    def RemoverPessoaPorMesa(self, mesa):
        pessoa_encontrada = None
        for pessoa in self.__registrarMorador:
            if isinstance(pessoa, (Morador, Locatario)) and pessoa.get_mesa() == mesa:
                pessoa_encontrada = pessoa
                print("=============================================================")
                pessoa_encontrada.exibir_informacoes()
                print("=============================================================")
                break
        
        if pessoa_encontrada:
            self.__registrarMorador.remove(pessoa_encontrada)
            self.__salvar_registro()
            print(f"A mesa {mesa} estava ocupada e a pessoa foi removida.")
        else:
            print(f"A mesa {mesa} está desocupada.")

    def AtualizarStatusPorMesa(self, mesa, novo_status):
        mesa = str(mesa)
        for morador in self.__registrarMorador:
            if isinstance(morador, Morador) and morador.get_mesa() == mesa:
                morador.set_statuspagamento(novo_status)
                self.__salvar_registro()
                break

    def PesquisarMesa(self, mesa):
        mesa = str(mesa)
        if mesa is not None:
            for morador in self.__registrarMorador:
                if isinstance(morador, Morador) and morador.get_mesa() == mesa:
                    return morador  # Retorna o objeto Morador encontrado
        return None # Mesa Desocupada
    
    def ObterStatusPorMesa(self, mesa):
        mesa = str(mesa)
        for morador in self.__registrarMorador:
            if isinstance(morador, Morador) and morador.get_mesa() == mesa:
                return morador.get_statuspagamento()  # Retorna o status de pagamento do Morador encontrado

    def ImprimirPessoa(self):
        frase = ""
        for morador in self.__registrarMorador:
            if isinstance(morador, Morador):
                frase = frase + "=============================================================\n" + str(morador.exibir_informacoes())
        return frase

                
    def __salvar_registro(self):
        with open(self.__arquivo, 'wb') as file:
            pickle.dump(self.__registrarMorador, file)

    
