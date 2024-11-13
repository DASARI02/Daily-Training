class Logic:
    def __init__(self):
        self.product = {}

    def place_order(self, Id):
        for i in self.product:
            if i.Id == self.product.Id: 
                return False 
        self.product.append(i)
        return True 
        

