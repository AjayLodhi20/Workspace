from abc import ABC, abstractmethod

class Discount(ABC):
    def __str__(self):
        return "this is a discount class"

    @abstractmethod
    def apply_discount(self, total_amount):
        pass

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total_amount):
        discount = total_amount * self.percentage
        return discount

class FlatDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, total_amount: float):
        if total_amount > self.amount:
            return total_amount - self.amount
        else:
            return "Discount is greater than amount"
