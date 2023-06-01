# Exercise 2 - Faulty calculator
# 45 * 3 = 555 , 56 + 9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following one
# 45 * 3 = 555 , 56 + 9 = 77, 56/6 = 4
# Your program should take operator and the two numbers as input from the user
# and then return the result

print("Enter 1st number:")
num1 = int(input())
print("Enter 2nd number:")
num2 = int(input())
print("what arthmatic calulation ?"+"+,-,/,*")
num3=input()
if num1==45 and num2==3 and num3=='*':
    print('555')
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1== 56 and num2 == 6 and num3 == '/':
    print("4")
elif num3 == '+':
    print(num1+num2)
elif num3 == '-':
    print(num1-num2)
elif num3 == '*':
    print(num1*num2)
elif num3 == '/':
    print(num1/num2)
else:
    print("Error!Please Check your input")


