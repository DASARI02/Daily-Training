class Update:
    def __init__(self, new_price, name):
        self.new_price = new_price
        self.name = name 

    def __str__(self):
        return f"name of the product{self.name}, price of the product{self.new_price}"