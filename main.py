from item import Item
# from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(11.0))

# phone1 = Phone("jscPhonev10", 500,5,1)
# print(phone1.calculate_total_price())
# phone2 = Phone("jscPhonev20", 700,5, 1)

# print(Item.all)
# print(Phone.all)

item1 = Item("MyItem", 750)
item1.name = "I have been changed by a Setter"

print(item1.name)