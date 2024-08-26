"""  Economy simulator """
# Basically the person has a central bank, they have to control the flow of money and how it works
# After that, they will be a random amount of banks that are created and the goal of the AIs is to
# predict How the economy will be like, and after that make a central bank that works in that favour

from enum import Enum

class Rank(Enum):
    """ Rank of each bank; A is highest and D is lowest"""
    A = 1
    B = 2
    C = 3
    D = 4

class CentralBank():
    """ Central Bank - The only thing the user can control """
    def __init__(self, name, base_interest_rate, money_available, staring_assets_value):
        self.name = name
        self.interest_rate = base_interest_rate
        self.money_available = money_available
        self.assets_value = staring_assets_value
        self.banks = [{}]

    def set_interest_rate(self, interest_rate: int):
        """ Setting interest rate """
        self.interest_rate = interest_rate

    def remove_money_from_cashflow(self, amount_removed: int):
        """ Removing money from the central bank's cashflow """
        if self.money_available < amount_removed:
            return -1

        self.money_available -= amount_removed
        return 0

    def add_money_to_cashflow(self, amount_added: int):
        """ Adding money to the central bank's cashflow """
        self.money_available += amount_added

    def add_bank(self, name: str, customers: int):
        """ Adding a bank to a central bank's index"""
        rank_thresholds = {
            Rank.A: 10000,
            Rank.B: 7000,
            Rank.C: 5000
        }

        rank = Rank.D  # Default rank
        for rank_value, threshold in rank_thresholds.items():
            if customers >= threshold:
                rank = rank_value
                break

        self.banks.append({
            "name": name,
            "customers": customers,
            "rank": rank
            })
