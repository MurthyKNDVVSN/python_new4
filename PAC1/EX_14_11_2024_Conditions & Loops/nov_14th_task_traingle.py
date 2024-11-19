# rougf logic
# accept 3 inputs which are int type
# o/p - A string will be the o/p

# logic building
# side1 = input("enter the lenght of side1:")
# -------
# Actual logic

def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("Not a Triangle")
    else:
        print("Not a Valid Length")


side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

result = classify_triangle(side1, side2, side3)
print(f"The triangle is classified as: {result}")
