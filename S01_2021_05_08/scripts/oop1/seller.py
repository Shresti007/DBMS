# CRUD:
class Seller:
    def __init__(self, s_id, name):
        self.s_id = s_id
        self.name = name

    def __str__(self):
        return f"ID: {self.s_id} Name: {self.name}"

    def __repr__(self):
        return self.__str__()
