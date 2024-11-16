# problem number to fix max b/t two numbers

# logic building
# 1. user inputs- > accept two interges
# 2. o/p --> int 1 which ever is grater max number it will return
# have to accept pi.3.14 or 45.67 float

num1 = float (input("enter number number1:"))
num2 = float(input("Enter number2 :"))
if num1 >= num2 :
    print("Max is " , num1)
else:
    print("max is " , num2)

# edge cases 1. if num1 and num2 are equal (if num1== num2)
# string --> ABC ,ten   --> for this we have to use try and exception
# -ve value also need to handle