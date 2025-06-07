from abc import ABC, abstractmethod

# ---------- Core Classes ----------

class PizzaBase:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class PizzaSize:
    def __init__(self, label: str, multiplier: float):
        self.label = label
        self.multiplier = multiplier

class PizzaTopping:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Beverage:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

# ---------- Discount Strategies ----------

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, pizza: 'Pizza', subtotal: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, subtotal):
        return subtotal

class SpecificBaseDiscount(DiscountStrategy):
    def __init__(self, base_name: str, percent: float):
        self.base_name = base_name
        self.percent = percent

    def apply_discount(self, pizza, subtotal):
        if pizza.base.name == self.base_name:
            base_discount = pizza.base.price * (self.percent / 100)
            return subtotal - base_discount * pizza.size.multiplier
        return subtotal

class SpecificToppingDiscount(DiscountStrategy):
    def __init__(self, topping_name: str, percent: float):
        self.topping_name = topping_name
        self.percent = percent

    def apply_discount(self, pizza, subtotal):
        discount = 0
        for t in pizza.toppings:
            if t.name == self.topping_name:
                discount += t.price * (self.percent / 100)
        return subtotal - discount * pizza.size.multiplier

# ---------- Pizza & Order ----------

class Pizza:
    def __init__(self, base: PizzaBase, size: PizzaSize, toppings: list[PizzaTopping], discount_strategy: DiscountStrategy = NoDiscount()):
        self.base = base
        self.size = size
        self.toppings = toppings
        self.discount_strategy = discount_strategy

    def calculate_price(self):
        topping_total = sum(t.price for t in self.toppings)
        subtotal = (self.base.price + topping_total) * self.size.multiplier
        final_price = self.discount_strategy.apply_discount(self, subtotal)
        return round(final_price, 2)

class Order:
    def __init__(self):
        self.pizzas = []
        self.beverages = []

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def add_beverage(self, beverage: Beverage):
        self.beverages.append(beverage)

    def calculate_total(self):
        total = sum(p.calculate_price() for p in self.pizzas)
        total += sum(b.price for b in self.beverages)
        return round(total, 2)

# ---------- Example Usage ----------

if __name__ == "__main__":
    base = PizzaBase("Thin Crust", 3.0)
    size = PizzaSize("Large", 2.0)
    toppings = [PizzaTopping("Cheese", 1.0), PizzaTopping("Olives", 0.5)]

    pizza1 = Pizza(base, size, toppings, discount_strategy=SpecificBaseDiscount("Thin Crust", 20))  # 20% off base
    pizza2 = Pizza(base, size, toppings, discount_strategy=SpecificToppingDiscount("Olives", 50))   # 50% off Olives
    pizza3 = Pizza(base, size, toppings)  # No discount

    coke = Beverage("Coke", 2.0)

    order = Order()
    order.add_pizza(pizza1)
    order.add_pizza(pizza2)
    order.add_pizza(pizza3)
    order.add_beverage(coke)

    print("Total Order Price:", order.calculate_total())
