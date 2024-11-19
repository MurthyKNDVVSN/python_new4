# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

n1 = int(input("Enter the n1 : "))
n2 = int(input("Enter the n2 : "))
n3 = int(input("Enter the n3 : "))


def sum_of_three(n1=100, n2=200, n3=400):
    return n1 + n2 + n3


result = sum_of_three()
print(result)

result2 = sum_of_three()
result3 = sum_of_three(10, 20)
result4 = sum_of_three(10, 30, 50)
result5 = sum_of_three(10, 30, 50, )
print(result2)
print(result3)
print(result4)
print(result5)