class Morador:
    def __init__(self, nome, endereco, comprovante, statuspagamento, mesa):
        self.__nome = self.set_nome(nome)
        self.__endereco = self.set_endereco(endereco)
        self.__comprovante = self.set_comprovante(comprovante)
        self.__statuspagamento = self.set_statuspagamento(statuspagamento)
        self.__mesa = mesa
        self._flagStatus = False
        self._flagMesa = False

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if not nome:
            raise ValueError("Nome do Proprietário em Branco! ")
        assert isinstance(nome, str), "Insira um nome válido!"
        self.__nome = nome
        return self.__nome
    
    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        if not endereco:
            raise ValueError("Endereço em Branco! ")
        assert isinstance(endereco, str), "Insira um endereço válido!"
        self.__endereco = endereco
        return self.__endereco

    def get_comprovante(self):
        return self.__comprovante

    def set_comprovante(self, comprovante):
        if not comprovante:
            raise ValueError("Link do Comprovante em Branco! ")
        assert isinstance(comprovante, str), "Insira um link de comprovante válido!"
        self.__comprovante = comprovante
        return self.__comprovante

    def get_statuspagamento(self):
        return self.__statuspagamento

    def set_statuspagamento(self, statuspagamento):
        assert isinstance(statuspagamento, str), "Insira um status válido!"
        if statuspagamento == "PAGO":
            self._flagStatus = True
            self.__statuspagamento = "PAGO"
        elif statuspagamento == "PENDENTE":
            self._flagStatus = False
            self.__statuspagamento = "PENDENTE"
        else:
            raise ValueError("Status de pagamento inválido!")
        return self.__statuspagamento

    def get_mesa(self):
        return self.__mesa

    def set_mesa(self, mesa):
        assert isinstance(mesa, str), "Insira uma mesa válida!"
        if not self._flagMesa:
            self._flagMesa = True
            self.__mesa = mesa
        else:
            raise ValueError("Mesa Ocupada, escolha outra!")

    def exibir_informacoes(self):
        frase = ""
        frase = (frase + f"Nome do Proprietario: {self.get_nome()}\n" + f"Endereco do Proprietario: {self.get_endereco()}\n" + 
                f"Comprovante: {self.get_comprovante()}\n" + f"Status do Pagamento: {self.get_statuspagamento()}\n" + f"Mesa: {self.get_mesa()}\n")
        return frase
        #print(f"Nome do Proprietario: {self.get_nome()}")
        #print(f"Endereco do Proprietario: {self.get_endereco()}")
        #print(f"Comprovante: {self.get_comprovante()}")
        #print(f"Status do Pagamento: {self.get_statuspagamento()}")
        #print(f"Mesa: {self.get_mesa()}")
