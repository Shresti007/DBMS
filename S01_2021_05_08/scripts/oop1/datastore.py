
class DataStore:
    __customers = {} #<c_id : Customer Object>
    __sellers = {} #<s_id : seller Object>
    __products = {}
    __seller_products = {} # <s_id : [p_ids]>

    def add_product(self, s_id, p):
        """
        Insert a new seller into the datastore
        """

        if s_id in self.__sellers:
            self.__products[p.p_id] = p
            temp = self.__seller_products.get(s_id, [])
            temp.append(p.p_id)
            self.__seller_products[s_id] = temp
            return True
        else:
            return False

    def get_product(self, c_id):
        return self.__products.get(c_id)

    def del_product(self, c_id):
        return self.__products.pop(c_id, None)

    def get_products(self):
        return self.__products.values()

    def get_products_for_seller(self, s_id):
        return self.__seller_products.get(s_id, [])

    def add_seller(self, s):
        """
        Insert a new seller into the datastore
        """
        self.__sellers[s.s_id] = s

    def get_seller(self, c_id):
        return self.__sellers.get(c_id)

    def del_seller(self, c_id):
        return self.__sellers.pop(c_id, None)

    def get_sellers(self):
        return self.__sellers.values()

    def add_customer(self, c):
        """
        Insert a new customer  into the datastore
        """
        self.__customers[c.c_id] = c

    def get_customer(self, c_id):
        return self.__customers.get(c_id)

    def del_customer(self, c_id):
        return self.__customers.pop(c_id, None)

    def get_customers(self):
        return self.__customers.values()
