import csv #imported csv module to use its features(methods,classes,attributes)
class Item:
    pay_rate = 0.8#this is a class attribute n can be accessed from both instance and class level
    all = []#this is also a class attribute
    #to use this class attribute and be able to have access to its values,we must either access them
    #...at the class or instance level
    #the take away here is that we can access a class attribute's value either at a class or instance level
    #list to which objects(instances) will be added upon instantiation
    def __init__(self,name:str,price:float,qty=0):#constructor special method to create attributes of object

        assert price >= 0, f"Price{price} is not greater than or equal to zero"
        assert qty >= 0, f"Qty {qty} is not greater than or equal to zero"
        #assign attributes to object
        self.name = name
        self.price = price
        self.qty = qty
        
    
    

        #Actions to execute
        """Since the constructor is called when creating instances, the code below will also be executed"""

        #access the class attribute from class level
        Item.all.append(self)#this code is responsible for adding instances to a list each time one is 
        #created

    def calculate_total_price(self):
        return self.price * self.qty

    def apply_discount(self):
        self.price = self.price * self.pay_rate#best practice to access class attribute from instance level

    @classmethod #class methods can only be accessed from a class level
    def instantiate_from_csv(cls):#this method is used to instantiate objects saved in a csv file
        #a class method is only accessed at a class level
        with open("OOP\items.csv","r") as f:#open csv file as f object
            reader = csv.DictReader(f)#convert what is in csv file into a dictionnary
            items = list(reader) #place the dictionnaries into a list where "items" contains the dictionnaries that were converted
            #this simply means that items is a list that contains each and every dictionnary that was converted from the csv file
            
            for item in items:
                #instantiate objects now, this code is now the one in charge of instantiating objects
                #call class to instantiate objects from it which are obtained from the items.csv file
                Item(name = item.get("name"),price = float(item.get("price")),qty = int(item.get("qty")))

        
        
    #mwdlbailvnorbwfk
    #The __repr__ dunder method is used to represent and display the object and helpful in debugging our code
    def __repr__(self):
        return f"Item({self.name},{self.price},{self.qty})"

#These are five instances each instance being appended to the 'all' items list when instantiated or at run time
item1 = Item("Phone",100,1)#first instance
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75, 5)

#Remember to access the value or values of the class attribute, we do this either from instance or class level

print(Item.instantiate_from_csv())
print(Item.all)



