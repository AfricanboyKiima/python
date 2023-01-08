class Item: 
    pay_rate = 0.8 #pay rate after 20% discount #this is a class attribute
    def __init__(self,name:str,price:float,quantity = 0):#constructor

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"


        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone",150,5)
print(item1.pay_rate)
print(item1.name)
print(item1.quantity)
print(item1.calculate_total_price())
print(Item.pay_rate)