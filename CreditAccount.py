from Product import Product
from Main_Bank_VersionX import *


class CreditAccount(Product, Account):

    def __init__(self, name, password, money):
        super().__init__(name, password, money)
        self.product_type = 'Credit'
        self.create_creadit = 10000
        self.credit_limit = 0.04
        

    def show_available_balance(self):
        print('Balance: ' + str(super().show()))

    