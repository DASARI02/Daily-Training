class Product:
    def __init__(self, Id, name, Price):
        self.ID = Id
        self.name = name 
        self.Price = Price

    def __str__(self):
        return {"product Id": self.ID,
                "product name": self.name,
                "Product Price": self.Price}
    

