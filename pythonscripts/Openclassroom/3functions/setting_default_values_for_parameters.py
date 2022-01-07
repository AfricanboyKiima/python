"""
In this script,i've written a function that has parameters that have default values
,this is to say that we can have parameters of a function having default values
by equating those parameters to a certain value
"""
def function(a=1,b=50,c=25):
    print("a=",a,"b=",b,"c=",c)
    store = a + b
    yes = c + a
    print("store =",store,"yes = ",yes)    
