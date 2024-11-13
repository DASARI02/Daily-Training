from logic import Logic 
from product import Product 

if __name__ == "__main__":
    a = Logic()

    p1 = Product(1, "Pizza", 500)
    p2 = Product(2, "Burger", 400)

    print(a.place_order(p1))
    print(a.place_order(p2))
    print(a.place_order(p1))

