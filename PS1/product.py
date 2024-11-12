class Product:
    def __init__(self, Id, name, Price):
        self.ID = Id
        self.name = name 
        self.Price = Price

    def __str__(self):
        return f"product {self.ID}, name of product {self.name}, price of product{self.Price}"
    


