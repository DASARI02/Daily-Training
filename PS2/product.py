class Product:
    def __init__(self, Id, name, Price):
        self.Id = Id
        self.name = name 
        self.Price = Price

    def __str__(self):
        return {"product Id": self.Id,
                "product name": self.name,
                "Product Price": self.Price}
    

