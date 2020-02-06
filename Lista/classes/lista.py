from classes.celula import Cell
from classes.my_exeption import List_empty

class Lista:
    def __init__(self):
        self.cabeca = Cell(0,None)
        self.ultimo = self.cabeca
        self._tam = 0
    
    def __str__(self):
        """Print the elements of list"""
        aux = self.cabeca.prox
        while(aux != None):
            print(aux.item)
            aux = aux.prox
        return "\n"

    def __len__(self):
        """Return the size of list"""
        return int(self._tam)
   
    def __getitem__(self, index):
        aux = self.cabeca
        
        for i in range(index):
            if aux.prox == None:
                e = List_empty()
                raise e
            else:
                aux = aux.prox

        return aux.item 
    
    def __setitem__(self, index, item):
        aux = self.cabeca
        
        for i in range(index):
            if aux.prox == None:
                e = List_empty()
                raise e
            else:
                aux = aux.prox

        aux.item = item
    
    def append(self, item):
        self.ultimo.prox = Cell(item, None)
        self.ultimo = self.ultimo.prox
        self._tam = self._tam + 1
    
    def search(self, item):
        aux = self.cabeca
        if aux.prox == None:
            e = List_empty()
            raise e

        while (aux.prox != None) :
            if aux.prox.item == item :
                return aux
            else:
                aux = aux.prox
        
        raise IndexError("There are not element in the list")
    
    def insert(self, index, item):
        if (index == 1):
            aux = self.cabeca
        else:
            elem = self.__getitem__(index)
            aux = self.search(elem)

        node = Cell(item, aux.prox)
        aux.prox = node

        self._tam = self._tam + 1

    def pop(self, item):
        aux = self.search(item)
        delet = aux.prox
        aux.prox = delet.prox
        delet = None
        self._tam = self._tam - 1 
        