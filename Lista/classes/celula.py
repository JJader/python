from classes.my_exeption import Invalid_value

class Cell:
    def __init__ (self, item, prox):
        """
        Item --> number
        prox --> Cell
        """
        self.item = item
        self.prox = prox
    
    @property
    def item(self):
        return self._item
    
    @property
    def prox(self):
        return self._prox
    
    @item.setter
    def item(self, item):
        if (type(item) is float or type(item) is int):
            self._item = item
        else: 
            e = Invalid_value()
            raise e

    @prox.setter
    def prox(self, prox):
        if (type(prox) is Cell or prox == None):
            self._prox = prox
        else: 
            e = Invalid_value()
            raise e

        