from package.fonctions import *
print(table(8))
#we've got he fonctions module that actually contains a function that can be imported if needed in any file
"""
The reason for creating packages is to be able to create a number of modules that contain the actual code
This actual code contained in the modules can then be imported at any level of the program as long as we just 
import the module. 
If an import statement begins with only import, this means everything in that module will be preceded by the name of 
the module to show where that particular thing is derived which leads to more readable code
In case we want to avoid that , we can then start with 'from module import *', we wont be required prefix the objects
obtained from the module with the module's name.
from package.module import is the way we deal with most modules to show a specific hierachy or path hence. we are able
to tell the computer where it should allocate specific modules that we want to use in a our program, these modules 
contain anything from : classes, methods, functions, variables and just anything we may want in our program
"""
