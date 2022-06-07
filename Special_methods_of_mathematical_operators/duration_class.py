"""
In this example we shall be looking at SM that allow us to overload mathematical operators.
"""
class Duration:
    """class containing number of durations expressed in number of minutes and number of seconds"""
    def __init__(self,min=0,sec=0):#python constructor without which we can't create attributes of our class
      self.min = min #number of minutes
      self.sec = sec #number of seconds
    def __str__(self):
        """display of our objects"""
        return "{0:02} : {1:02}".format(self.min,self.sec)
