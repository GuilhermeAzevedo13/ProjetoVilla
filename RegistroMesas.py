import pickle
import os

class RegistroMesasOcupadas():
    def __init__(self, arquivo='registroMesas.dat'):
        self.__mesas_ocupadas = []
        self.__arquivo = arquivo

        if not os.path.exists(self.__arquivo):
            with open(self.__arquivo, 'wb'):
                pass  # Cria um arquivo vazio

        try:
            with open(self.__arquivo, 'rb') as file:
                self.__mesas_ocupadas = pickle.load(file)
        except (FileNotFoundError, EOFError):
            pass
    
    def get_mesaOcupada(self):
        return self.__mesas_ocupadas
        
    def InserirMesaOcupada(self, mesa):
        self.__mesas_ocupadas.append(mesa)
        self.__salvar_registro()
        
    def RemoverMesaOcupada(self, mesa):
        self.__mesas_ocupadas.remove(mesa)
        self.__salvar_registro()
        
    def __salvar_registro(self):
        with open(self.__arquivo, 'wb') as file:
            pickle.dump(self.__mesas_ocupadas, file)