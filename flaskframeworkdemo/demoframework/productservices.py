from abc import ABC,abstractmethod

class ProductServices(ABC):

    @abstractmethod
    def add_product_in_stock(self):
        pass

    @abstractmethod
    def modify_existing_product_details(self):
        pass

    @abstractmethod
    def check_product_availble_in_stock_or_not(self):
        pass

    @abstractmethod
    def fetch_list_of_products(self):
        pass