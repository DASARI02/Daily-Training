# class Logic:
#     def __init__(self):
#         self.product = []
    
#     def add_product(self,new_product):
#         for i in self.product:
#             if i.ID == new_product.ID:
#                 return False
#         self.product.append(new_product)
#         return True
#     def update_product(self, product):
#         for i in range(len(self.product)):
#             if 
        
    
class Logic:
 
    def __init__(self):
        self.Products = []
 
 
 
    def addProduct(self, new_product):
        for nproduct in self.Products:
            if nproduct.productId == new_product.productId:              
                return False
        self.Products.append(new_product)
        return True
 
 
 
    def updateProduct(self, productId, new_name, new_price):
        for uProduct in self.Products:
            if uProduct.productId == productId:
                uProduct["ProductName"] = new_name
                uProduct["ProductPrice"] = new_price
                # print(f"Product {productId} Updated: \nName: {newName} \nPrice: {newPrice}")
                return
        #print("Task Not Found")
 
 
 
    # def viewProducts(self):
    #     print(self.Products)
 
 
 
    # def applyDiscount(self, discountPercentage):
    #     if discountPercentage < 0 or discountPercentage > 100:
    #         print("Invalid discount percentage.")
    #         return
       
        # for ADproduct in self.Products:
        #     originalPrice = ADproduct.productPrice
        #     discountPrice = originalPrice - (originalPrice * discountPercentage / 100)
        #     ADproduct.productPrice = round(discountPrice,2)
        #     print(f"Discount applied to {ADproduct.productName}, \nOriginal Price {originalPrice}, \nAfter Discount {ADproduct.productPrice}")
       
       

    def update(self, product):
        for i in self.product:
            if i.ID == product.ID:
                return True       