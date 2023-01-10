class Item: 
    """This thing works like global and local scopes remember when we are working with scopes variables within the 
    the functions are said to exist in the local scope while variables outside functions are said to exist 
    in the global scope. A scope is like a container for variables and remember when dealing with the local scope,
    it is destroyed when the functions returns such that the values that were assigned to the variables are
    forgotten and it is for this reason that variables outside functions can not access the values of the 
    variables within functions since these values are forgotten when the function call returns
    """
    """
    Now here what we are trying to understand is that when we create class attributes, we can access them from 
    the instance and class level so when we actually instantiate an object from a class, that object ofcourse
    knows that that attribute it is seeking is not assigned to it and so it actually seeks for the attribute
    from the class where this attribute is said to be a class attribute which can be accessed by both
    the instances and classes as we tested in the code below 
    """
    pay_rate = 0.8 #pay rate after 20% discount #this is a class attribute
    def __init__(self,name:str,price:float,quantity = 0):#constructor

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"


        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):#action performed on object
        return self.price * self.quantity

    #CREATE METHOD THAT WILL GRANT DISCOUNT ON OUR ITEM PRICES
    def apply_discount(self):#action performed on object
        #here we are basically applying a discount on our item prices and this happens only on the prices and when the apply_discount() method is
        #called
        self.price = self.price * self.pay_rate   #we accessed the class attributes from the class level(Item.pay_rate) but later changed to object level(self.pay_rate)

        #the above statement is the same as saying self.price = self.price * Item.pay_rate

item1 = Item("Phone",100,1)#Instantiated object from the Item class and therefore composed of the attributes assigned to object after constructor
item1.apply_discount()
#print(item1.price)  
#print(item1.calculate_total_price())


#Assign a discount to specific item only such as a laptop in our case

item2 = Item("Laptop",1000,3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

""" When dealing with a scenario where we would want to apply a discount at the for a specific product amongst out items
, it is best practice to actually access the class attribute from an instance level in the case of our 
apply_discount() method, so that in such a case, if we are to assign a discount for a specific instance,
we can access the class attribute at the instance level
"""