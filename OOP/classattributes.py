"""WE ARE LOOKING AT CLASS ATTRIBUTES HERE"""


class Item:#class is a model which simply means it represents an idea or theory 
    pay_rate = 0.8#class attribute
    def __init__(self,name:str, price:float,quantity = 0):#constructor to create attributes of our object

        assert price >= 0, f"Price {price} is not greater than or equal to zero "
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero "

        #assign to self object
        self.name = name #attributes are characteristics of the object
        self.price = price
        self.quantity = quantity 
    
    def calculate_total_price(self):

        return self.price * self.quantity


item1 = Item("Phone",100,1)
item2 = Item("Laptop",1000,3)


print(Item.__dict__)#this gives all the attributes at the class level
print(item1.__dict__)
print(item2.__dict__)
