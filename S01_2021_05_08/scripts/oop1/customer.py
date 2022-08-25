class Customer:
    def __init__(self, c_id, name):
        self.c_id = c_id
        self.name = name

    def __str__(self):
        return f"ID: {self.c_id} Name: {self.name}"

    def __repr__(self):
        return f"ID: {self.c_id}"


