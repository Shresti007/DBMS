class Flat:
    def __init__(self):
        self.type = "premium"
        self.__bhk = "3 BHK"

flat_1 = Flat()
print(flat_1.type)


 flat_1.__bhk()


class Savingacc2:
    __accno = 456

# to allow access we use get a method
    def get_accno(self):
        return self.__accno


ob2 = Savingacc2()
print(ob2.get_accno())
