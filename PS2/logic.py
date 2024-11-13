class Logic:
    def __init__(self):
        self.product = []

    def place_order(self, Id):
        for i in self.product:
            if i.Id == Id.Id: 
                return False 
        self.product.append(Id)
        return True 
    def view_all(self):
        return self.product
        


