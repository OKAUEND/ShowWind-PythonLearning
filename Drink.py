from MenuItem import MenuItem

class Drink(MenuItem):
    def __init__ (self,name,price):
        super().__init__(name,price)

    def info(self):
        return self.name + ':￥' + str(self.price) 