# MODULES
"""
A module is a file that contains source code. The main
purpose of modules is to group Python functions and
objects in order to organize larger projects. Note that in
addition to Python code, we can also import C++ object
files.
"""
# Let's see then how to create a new modules and how we can use it.
#
# import my_double
# print(my_double.some_variable)
# print(my_double.my_double.__doc__)

'''
In the previous example, we had to write the module name
each time we wanted to use an object. In order to directly
use an object, we can use the following syntax:

from module_name import object_name1, object_name2,…

Moreover, if we want to import all functions and objects
within the module, we can also use the following syntax:

from module_name import *(object_name1, object_name2,..)
'''


from my_double import *
print(my_double(5))


