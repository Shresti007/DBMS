from seller import Seller
from datastore import DataStore
from product import Product
from customer import Customer

from datetime import datetime

from foo import bar

# driver code
if __name__ == '__main__':
    d = DataStore()

    d.add_seller(Seller(1,"gaurav"))
    d.add_seller(Seller(2,"gaurav2"))

    print(d.get_sellers())

    print("add status", d.add_product(1, Product(1,"Covaxine", "medicine", 250, 10)))
    print("add status", d.add_product(3, Product(2,"Covishield", "medicine", 250, 10)))

    print(d.get_products())

    print(d.get_products_for_seller(1))
    print(d.get_products_for_seller(2))
