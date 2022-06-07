"""
we are looking at container objects and understanding deeply what SM are called when we overload operators with indexes,we even go above and beyond to deeply understand the inner workings
by creating what is known as an envelopped class. Envelopped classes are literraly classes that ressemble other classes but are not actually classes. We create a class composed of an attribute that is
a dictionnary and won't be accessed from outside of the class i.e _dictionnary . The object coming from our class called ZDict will be such to it is passed and index through its operator(square brackets), in
such a case,self._dictionnary[index] will be returned. Let's go ahead and dive deep into the inner workings.
"""
class ZDict:#our envelloped class that will resemble our normal classes but won't actually be a class
    def __init__(self):
        #our class is composed of an attribute which won't be accessed from outside of the class
        self._dictionnary = {}#attribute is actually a dictionnnary which means the objects coming from this class will container a container datatype,hence xtised a dictionnary
    def __getitem__(self,index):
        #when we tap object[index],it is the __getitem__ SM that is called, so to this SM is passed the index that was passed to the object's operator hence overloading taking places
        #By overloading,we refer to telling python what to do when it's using a specific operator.
        return self._dictionnary[index]
    """
The thing to understand deeply here is that if you look at the attribute's value, one finds that it's equated to a dictionnary,
and we are told that when an object comes from a class it is able to use the attributes as well as the methods of that class,
in our case,the issue is that our object will actually be a dictionnary and just like any other container object,we can access the elements within by overloading operators since
each element in a container object is referenced by an index or key depending on the data type that one is using. In our example if we say object[index],the getitem__ SM is called in such a way that
the "self._dictionnary[index] is what is returned,in my view and understanding ,I see that since the object is from the class and attributes are contained in objects,we can have a close look at the
object and what is returned,remember the attribute was equated to a dictionary and therefore it is actually a dictionnary,now we see the return value from the getitem SM is actually that
same attribute except that to it is now attached an operator which is overloaded with an index. this simply means that that same dictionnary returns the item at that index that is passed
 to it, the one confusing thing may be the self parameter that is attached to the attribute,this simply means that the object will be able to use the attribute and therefore enabling python to
 return the return value to the object that would have come from that class therefore enabling our object to be able to return the elements at the passed index in the operator.
"""
    def __setitem__(self,index,val):
        self._dictionnary[index] = val
