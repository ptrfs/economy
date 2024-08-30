""" The different types of markets in an economy """
import asyncio
from enum import Enum
from dataclasses import dataclass
from eco import CentralBank

class BondMarketActionType(Enum):
    """ Bond Market: Action type """
    SELL_BOND_START = 1
    SELL_BOND_END = 2
    REPAY_BOND = 3

@dataclass
class BondMarketAction:
    """ Bond Market: Bond market action type """
    type: BondMarketActionType
    amount: int
    repay_amt: int = None
    bond_price: int = None

class BondMarket:
    """ Bond Market: The Central Bank can sell government bonds at a rate 
    that they'll need to repay later"""
    def __init__(self, central_bank: CentralBank):
        self.central_bank = central_bank
        self.buyers = [{}]
        self.market_events = asyncio.Queue(2)

    def add_buyer(self, name: str):
        """ Adding buyer """
        self.buyers.append({
            "name": name,
            })

    async def broadcast_bond_market_action(self, action_type: BondMarketActionType):
        """ Broadcast something to the bond market """
        await self.market_events.put(action_type)

class BondMarketBuyer:
    """ Bond Market: Buyer """
    def __init__(self, name: str, purchasing_amount, max_bond_taking_amount, min_bond_amt):
        self.name = name
        self.purchasing_amount = purchasing_amount
        self.max_bond_amt = max_bond_taking_amount
        self.min_bond_amt = min_bond_amt
        self.bonds = 0

    def get_name(self):
        """ Getting name """
        return self.name

    def get_purchasing_amt(self):
        """ Getting amount avaibale for the buyer """
        return self.purchasing_amount

    def sell(self, amt: int, price: int):
        """ Sell bonds """
        i: int = 0
        while i < amt:
            self.bonds -= 1
            self.purchasing_amount += price
            i += 1

    def response(self, action: BondMarketAction):
        """ Doing something based on the response """
        match action.type: # i hate myself so much for this
            case 1:
                if self.bonds == self.min_bond_amt:
                    return -1

                self.bonds += 1
                self.purchasing_amount -= action.bond_price
                return 0
            case 2:
                pass
            case 3:
                self.sell(action.repay_amt, action.bond_price)
            case _:
                pass

    async def listen_and_respond(self, bond_market: BondMarket):
        """ Listen and respond to action """
        while True:
            item = await bond_market.market_events.get()
            await self.response(item)
            bond_market.market_events.task_done()

