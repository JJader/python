class Banco_de_dados:
    def __init__(self):
        self.__dados = {} # private
        self.__nome = 'joao'
    
    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome} 
        else:
            self.__dados['clientes'].update({id : nome})
    
    def imprimir_clientes(self):
        for id,nome in self.__dados['clientes'].items():
            print(f'{id} : {nome}')

    def excluir_cliente(self, id):
        try:
            del self.__dados['clientes'][id]
        except:
            print("Cliente não encontrado")
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor