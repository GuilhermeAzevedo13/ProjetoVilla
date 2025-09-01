from Morador import Morador

class Locatario(Morador):
    def __init__(self, nome, endereco, comprovante, statuspagamento, mesa, nome_locatario, telefonelocatario):
        super().__init__(nome, endereco, comprovante, statuspagamento, mesa)
        self.__nome_locatario = self.set_nome_locatario(nome_locatario)
        self.__telefonelocatario = self.set_telefonelocatario(telefonelocatario)

    def get_nome_locatario(self):
        return self.__nome_locatario
    def set_nome_locatario(self, nome):
        if not nome:
            raise ValueError("Nome do Locatário em Branco! ")
        assert isinstance(nome, str), "Insira um nome válido!"
        self.__nome_locatario = nome
        return self.__nome_locatario

    def get_telefonelocatario(self):
        return self.__telefonelocatario
    def set_telefonelocatario(self, telefone):
        if not telefone:
            raise ValueError("Número de Telefone em Branco! ")
        assert isinstance(telefone, str), "Insira um telefone válido!"
        if len(telefone) == 11:
            self.__telefonelocatario = telefone
        else:
            raise ValueError("Insira um telefone válido com o formato correto (DD) 9XXXX-XXXX, por exemplo: (79) 99652-3665.")
        return self.__telefonelocatario

    def exibir_informacoes(self):
        frase = ""
        frase = (frase + "Nome do Locatario: {}\n".format(self.get_nome_locatario()) + "Telefone: {}\n".format(self.get_telefonelocatario()) + super().exibir_informacoes())
        #print("Nome do Locatario: {}".format(self.get_nome_locatario()))
        #print("Telefone: {}".format(self.get_telefonelocatario()))
        #super().exibir_informacoes()
        return frase
