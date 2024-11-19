# User Defined
# 1. The can't return -> non return
# 2.They can't return anything or  No return type with parameters/Arguments
# 3.They have parameters
# 4. They don't parameters / arguments



# 1. The can't return -> no return value

# no return type and no parameters/ Arguments - NRNP
def cricket():
    print("Welcome to PYTHON")
cricket()

# 2 . No return type with parameters/Arguments
def greet(name):
    print(F"Hello {name}")
    print(F"Hello" + "Murthy")
greet("Murthy")

# No return type with default arguments
def greet_default(name = "murthy"):
    print("Hello"  + " KANDAVALLI")
    print(f"Hello {name.upper()}")

greet_default()
def multi_args(name1="A", name2="B"):
    print(f"Mul --> {name1.upper(),name2.upper()}")

multi_args()
multi_args(name1= "MURTHY" , name2="Kandavalli")
multi_args(name2="Valli")
multi_args(name1="ROGGER" , name2="VALLI")
multi_args(name2="KANDAVALLI")

# 4. Arguments with return type
def sum(a,b):
    return a + b
result = sum(a=5,b=10)
print(result)

def sum_of_two(a1 = 100, b1=200):
    return a1+ b1

result = sum_of_two(a1=30,b1=50)
print("SUM OF TWO NUMBERS", result)
result= sum_of_two()
print(result)