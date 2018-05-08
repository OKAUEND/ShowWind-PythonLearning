from MenuItem import MenuItem

class Food(MenuItem):
    """description of class"""
    def __init__(self, name , price ,calorie):
        super().__init__(name,price)
        self.calorie = calorie

    def info(self):
        return self.name + ':￥' + str(self.price) + ' ' + str(self.calorie) + 'kcal'
