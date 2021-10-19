from item import Item
from keyboard import Keyboard

item1 = Item("MyItem", 750, 6)
keyboard1 = Keyboard("MyKeyboardItem", 750, 6)

keyboard1.apply_discount()
print(keyboard1.price)