class MenuItem(object):
    """description of class"""
    def __init__(self, name,price):
        self.name = name
        self.price = price

    def Total_price(self,Order_Count):
        return self.price * Order_Count

