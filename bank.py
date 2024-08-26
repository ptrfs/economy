""" Bank class """
from eco import CentralBank

class bank:
    """ A bank, that can be both commercial and consumer"""
    def __init__(self, name, money_available: int, central_bank: CentralBank, projected_customers):
        self.name = name
        self.money_available = money_available
        self.central_bank = central_bank
        self.customers = [{}]
        self.notify_central_bank(projected_customers)

    def notify_central_bank(self, potential_customers: int):
        """ Telling the central bank that we exist """
        self.central_bank.add_bank(self.name, potential_customers)

