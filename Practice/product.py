class Product:
    _id_increment = 1
    def __init__(self, name: str, price: float):
        self.product_id = Product._id_increment
        self.name = name
        self.price = price
        Product._id_increment += 1

    def get_shipping_cost(self):
        return self.price

class PhysicalProduct(Product):
    def __init__(self,name:str, price:float, weight_kg: float):
        super().__init__(name, price)
        self.weight_kg = weight_kg
        self.base_fee_dollars = 5

    def get_shipping_cost(self):
        super().get_shipping_cost()
        additional_fees = 2 * self.weight_kg
        total_fees = self.base_fee_dollars + additional_fees
        return total_fees

class DigitalProduct(Product):
    def __init__(self, name:str, price:float, url:str):
        super().__init__(name, price)
        self.download_url = url






