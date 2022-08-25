class Donation:
    def __init__(self, amount):
        self.__amount= amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self,amount):
        if amount<10:
            return self.__amount == 10
        elif amount > 1000000:
            return self.__amount == 1000000
        else:
            self.__amount == amount

Charity= Donation(5)
charity.amount()























