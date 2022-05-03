class Product:
    def __init__(self,p_name,p_price,p_qty):
       self.p_name = p_name
       self._p_price = p_price
       self.p_qty = p_qty#these are the attributes of my object which means every object from this class will be composed of a name,price and qty
    #lets create other methods to enable us deal with OOPS and even learn it more deeply. we shall also be dealing with encapsulation which enables us hide some data of our object
       #let's say we do not want these attributes to be accessed from outside of the class so this will call for encapsulation
    def _get_p_price(self):
        return self._p_price
    def _set_p_price(self,new_value):#python convention states that when an attribute or group of attributes begins with an underscore,we can't access it from the outside of the class
        self._p_price = new_value
    """
remember in other programming languages such as c++ and java,there are mechanisms put in place that define whether an attribute or group of attributes can be accessed from outside of the class,
when an attribute or a group of attributes is in the public class,we can access them from the outside of the class,but when in the private class,we can't but have to use accessors and mutators to deal
with accessing and modifying respectively.
In python,the mechanisms of access to attributes is quite different since there are no private objects as everything is public.
However,to deal with encapsulation,python has a mechanism called properties that enable it to deal with encapsulation,this whole principle of not having access to attributes from outside of the class is
referred to as encapsulation which involves hiding the data of an object so instead of having a private class,python instead brings in the principle of properties to deal with encapsulation of
attributes making it the most transparent way of manipulating attributes of an object.
WHEN DEALING WITH ENCAPSULATION,THE MOST TRANSPARENT WAY OF MANIPULATING ATTRIBUTES OF AN OBJECT IS BY USING PROPERTIES.
"""
    #so properties are basically like the private class in c++ and java. they are the ones that enable us deal with encapsulation.
    #these receive normally four methods. but the most passed to them are a getter and a setter or accessor and mutator respectively
    price = property(_get_p_price,_set_p_price)
    
    
