from Product import Product
from Main_Bank_VersionX import *

class SavingsAccount(Product, Account):
    def __init__(self, name, password, money):
        super().__init__(name, password , money)
        self.product_type = 'CASA'

    def show_available_balance(self):
        print('Balance: ' + str(super().show()))

        