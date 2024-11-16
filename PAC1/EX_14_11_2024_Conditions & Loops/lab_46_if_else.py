# problem find the max b/w three
# logic builing
# user input - num1,num2,num3
# o/p --> int or string with max number

# logic if condition1 :
# print("do 1 ")
# else if condtion2 :
# print("do 2")
# else if con3
# print(do 3)
# else :
# print("do for else")

NUM1 = int(input("ENTER THE NUMBER1\n"))
NUM2 = int(input("ENTER THE NUMBER2\n"))
NUM3 = int(input("ENTER THE NUMBER3\n"))

if NUM1 > NUM2 and NUM1 > NUM3:
    print("Max is", NUM1)
elif NUM2 > NUM1 and NUM2 > NUM3:
    print("Max is :", NUM2)
else:
    print("Max is:", NUM3)
