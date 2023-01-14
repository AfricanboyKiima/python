class Item: #model which is an informative representation of an object
    pay_rate= 0.8
    def __init__(self,name:str,price:float,quantity=0):#python constructor to create object attributes

        assert price >= 0, f"Price {price} is not greater than or equal to zero" #we are avoiding negative values here by ensuring the numbers given are positive
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        self.name = name 
        self.price = price
        self.quantity =quantity
    
    def calculate_total_price(self): # calculates total price of the commodity bought
        return self.price * self.quantity

    def apply_discount(self):
            self.price = self.price * self.pay_rate
       
item1 = Item("Switch",560,7)#create this item1 object that becomes of the Item
item1.apply_discount()
print(item1.price)