from abc import ABC, abstractclassmethod

class Product(ABC):
    product_type = ''

    @abstractclassmethod
    def show_available_balance():
        pass