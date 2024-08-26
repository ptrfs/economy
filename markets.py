""" The different types of markets in an economy """
from eco import CentralBank

class BondMarketBuyer:
    def __init__(self,)

class BondMarket:
    """ Bond Market: The Central Bank can sell government bonds at a rate 
    that they'll need to repay later"""
    def __init__(self, central_bank: CentralBank):
        self.central_bank = central_bank
        self.buyers = []
