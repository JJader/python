class Pessoa:
    def __init__(self, nome, idade):
        """Referente a intância, como modificar um atributo"""
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("...Falando...")

    @classmethod
    def por_ano_nascimento(cls, nome,ano_nascimento):
        """Referente a classe, como criar uma nova classe"""
        idade = 2019 - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        """Não é referente nem a classe nem a instancia"""
        pass

    @property
    def nome(self):
        """Getter"""
        return self._nome

    @nome.setter
    def nome(self, valor):
        """setter"""
        self._nome = valor