import csv
class Item:
    all = []
    pay_rate = 0.8
    def __init__(self,name:str,price:float,qty=0):#constructor to enable creation object attributes

        assert price >= 0, f"Price {price} is not greater than or equal to zero "
        assert qty >= 0, f"Quantity {qty} is not greater than or equal to zero "
        
        #Assign attributes to object
        self.name = name
        self.price = price
        self.qty =qty

        #add each instance created to the all list which acts as some temporary db to contain every object
        Item.all.append(self)

    def calculate_total_price(self):
        
        return self.price * self.qty
    
    def __repr__(self):

        return f"Object composed of values {self.name},{self.price},{self.qty} and attributes name, price and qty respectively" 
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("OOP/items.csv","r") as f:
            resources = csv.DictReader(f)
            items = list(resources)

        for item in items:

            Item(name= item.get("name"),price= item.get("price"), qty= item.get("qty"),)