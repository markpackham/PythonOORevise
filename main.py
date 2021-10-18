class Item:

    # Pay rate after 20% discount
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=1):
        # Run validations on arguments
        assert price > 0 and quantity > 0, f"Price {price} and quanity {quantity} must be great than zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
        

item1 = Item("Phone",100.51,5)
item2 = Item("Laptop",1000,3)

print(Item.pay_rate)
