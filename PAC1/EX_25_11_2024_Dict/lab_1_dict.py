from symbol import for_stmt

my_dict = {
    "name": "Aman",
    "Age": 32,
    "role": "qa",
    "Experience": "10 Yers"
}
# Accessing Values : my_Dict[key]
print(my_dict["name"])
print(my_dict)
print(my_dict["Age"])
my_dict["role"] = "Automation Engineer"
print(my_dict)
for key,value in my_dict.items():  # for iterating values in the dict ---> for key,value in my_dict.items():
    print(key,  "----> ",value)
del my_dict["Age"]  # deleting an item from the dict
print(my_dict)
print("Age" in my_dict)
print("role" in my_dict)