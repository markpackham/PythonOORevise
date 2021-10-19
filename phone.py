from item import Item

class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity=1, broken_phones=0):
        # Use super to get parent's abilities
        super().__init__(
            name,price,quantity
        )

        self.broken_phones = broken_phones