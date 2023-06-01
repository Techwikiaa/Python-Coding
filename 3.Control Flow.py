# Control Flow: Python offers many different structures to control the program execution and flow,such as conditional and loop statements;let's take a look at them in detail.
# if-else
'''
<              Less than
<=             Less than or equal
==             Equal
>              Greater than
>=             Greater than or equal
!=             Not equal is
is not         Object identity / negate
in / not in    Is inside / negate
And            Logical AND
Or             Logical OR
Not            Logical NOT

'''
# if-else statements
# This program check if the user value is true or false
'''
if 1==2:
    print('You have condition:',True)
else:
    print("sorry condition is:",False)
'''

# The above program checks if the user value is greater than
# or equal to 10. Depending on the value provided,
'''
user_value = int(input("Enter a number: "))
if user_value >= 10:
    print("The value enter is greater or equals 10")
    flag = True
else:
    print("The value is less than 10")
    flag = False
print(flag)

'''

# if-elif-else statements
'''
print("Choose an option: \n\t1) sum\n\t2) sub\n\t0) exit")
u_value = input("Enter an option: ")
if u_value == "0":
    print("Bye")
elif u_value == "1":
    print("sum operations")
elif u_value == "2":
    print("sub operations")
else:
    print("Wrong option")
'''

# if statements can be nested:
# Python offers two loops:
# while and for
#This program us numbers of sum form 0 to a given numbers
# uservalue = int(input("Enter a number:"))
# i = 0
# j = 0
# while i <= uservalue:
#     j = j + i
#     i += 1
# print("result is",j)

# Let’s say we want to write a program
# that calculates the exponential value
# (^2) of all the even numbers in the
# range from 0 to a given number.


# x = int(input("Enter a number:"))
# for i in range(0,x,2):
#     print(i,"^2 = ",i**2)