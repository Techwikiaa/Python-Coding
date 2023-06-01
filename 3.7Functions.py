# A function is a group of statements that gets executed
# when it is called (function call).

# The general form of a function definition is:
def my_sum(x,y):
    """Return the sum hello"""
    return x+y
# The return value is associated
# to variable x
# x = my_sum(5,6)
# print("sum is:", x)
#
# # print the function value
# print(x)
#
# # print the function doc
# print("My_sum doc:",my_sum.__doc__)








# One of the most important things when using functions is to
# understand the scope of variables. In Python, each call to a
# function creates a new local scope as well as all the assigned
# names within a function that are local to that function.


# x = 10
# # Variable z and f are local and# can only be used within
# # the function
# def test_scope(z):
#     f = x + z
#     return f
# print("Before test_scope x is ",x)
# print("This is test_scope result:",test_scope(2))
# print("after test_scope x is ",x)


# Global variables can be used within the function
# def change_global ():
#     """Return the sum"""
#     global x
#     x = 1
# x = 4
# print("x before calling the function",x)
# change_global ()
# print("x after calling the function ",x)

















# parameters : paramaters are usually passed by position;this mean
# that when we call afunction, the parameters in the calling
# function are matched according to their order.


# so the number of parameters used by the caller and the called
# function must be the same; otherwise,an expection will be raised

# eLearnSecurity 2013
""" Another useful feature consists of assigning functions to
variables.
Once a variable refers to a function, it can be used in the
same way as the function. """
# def by_name(x,y):
#     return x-y
# res = by_name(y = 30,x = 10)
# print(res)

''' Shown in the following code which is similar to the switch seen 
before ,this can be very useful in conjuction with dictonaries.'''

# Write a program to take two input from users for sum and multiplication
# using directory

def a(x):
    print("sum of ",x,"+",x)
    return x + x
def b(x):
    print("Mul of ",x,"*",x)
    return x * x

function_switch = {
    1:a,
    2:b,
}

user = int(input("""Select the operation:
1) sum
2) Mul
"""))

if user in function_switch:
    x = int(input("Enter a number: "))
    result = function_switch[user] (x)
    print("result is ",result)
else:
    print("Invalid Number")


# result = function_switch [1](5) is then executed.
# Since the value of function_switch [ is a , the function a(5) is
# called,and the result is stored in the variable result
