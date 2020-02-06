class Invalid_value(Exception):
    def __init__(self):
        self.mensagem = "the value is not permited"
    
    def __str__(self):
        return repr(self.mensagem)

class List_empty(Exception):
    def __init__(self):
        self.mensagem = "there are no element in this index"
    
    def __str__(self):
        return repr(self.mensagem)

    
    