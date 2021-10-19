import csv

class Item:

    # Pay rate after 20% discount
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=1):
        # Run validations on arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # Property Decorator = Read-Only Attribute
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 1000:
            raise Exception("The name is TOO LONG!!!!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # represent objects eg print(Item.all) gives
    # [Item (Phone,100,1), Item (Laptop,1000,3), Item (Cable,10,5), Item (Mouse,50,5), Item (Keyboard,75,5)]

    # item1 = Item("Phone", 100, 1)
    # item2 = Item("Laptop", 1000, 3)
    # item3 = Item("Cable", 10, 5)
    # item4 = Item("Mouse", 50, 5)
    # item5 = Item("Keyboard", 75, 5)

    # for instance in Item.all:
    #     print(instance.name)

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )


    @staticmethod
    def is_integer(num):

        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name},{self.price},{self.quantity})"
    
    # @property
    # def read_only_name(self):
    #     return "AAA"