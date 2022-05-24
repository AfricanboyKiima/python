class ZDict:
    def __init__(self):#python constructor that enables us to create attributes of our class without which it is impossible to create our attributes
        self._dictionnary = {}
    def __getitem__(self,index):#this is in charge of returning the values at the indexes passed to it.
        return self._dictionnary[index]
    def __setitem__(self,index,val):
        self._dictionnary[index] = val
    def __contains__(self,element):
        if element in self._dictionnary:
            return True
        else:
            return False
    def __repr__(self):
        return "This object is composed of the attribute _dictionnary"
