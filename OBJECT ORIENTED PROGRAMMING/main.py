from OOP.items import Item #we are importing a class here
from OOP.phone import Phone #same applies here

Item.instantiate_from_csv()
print(Item.all)