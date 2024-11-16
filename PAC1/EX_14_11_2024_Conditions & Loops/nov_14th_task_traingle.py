# rougf logic
# accept 3 inputs which are int type
# o/p - A string will be the o/p

# logic building
# side1 = input("enter the lenght of side1:")
# -------
# Actual logic

SIDE1 = int(input("ENTER THE LENGTH OD SIDE1 :\n"))
SIDE2 = int(input("ENTER THE LENGTH OD SIDE2 :\n"))
SIDE3 = int(input("ENTER THE LENGTH OD SIDE3 :\n"))

if SIDE1 == SIDE2 == SIDE3:
    print("IT IS equilateral Traingle")
elif SIDE1 == SIDE2 or SIDE2 == SIDE3 or SIDE1 == SIDE3:
    print("IT IS A isosceles Traingle")
else:
    print("IT IS A scalene Traingle")
