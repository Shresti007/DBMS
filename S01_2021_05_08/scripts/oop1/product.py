class  Product:
    def __init__(self, p_id,name,category,price,quantity):
        self.p_id = p_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"p_id = {self.p_id} name = {self.name} category = {self.category} price = {self.price} quantity = {self.quantity}"

    def __repr__(self):
        return self.__str__()
