class Logic:
    def __init__(self):
        self.products = []  

    def add_product(self,new_product):
        for i in self.products:
            if i.ID == new_product.ID:
                return False
        self.products.append(new_product)
        return True

    def update_product(self, product_id, updated_product):

        for product in self.products:
            if product.ID == product_id:
                product.name = updated_product.name
                product.price = updated_product.new_price
                return True
        return False

    def discount (self, discounted_product):
        if len(self.products):
            for i in self.products:
                va_price = i.Price*(discounted_product/100)
                i.Price -= va_price
            return self.products
        else:
            return False

    def view_all(self):
        return self.products
   
        

            
    
