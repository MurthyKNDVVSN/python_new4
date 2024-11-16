# write a program  to take a user age and
# let him know if he go the club
# 21

# Write  logic building formula

# step-1
# user input data type -> int
# O/P string -> user if he can go or not

# STEP-2 Rough logic( Brute force logic)
# age > = 21 can go to club
# age <  21 can't go to club

# Step 3 --> Actual logic

age = input("Enter your AGE:")
age = int(age)

if age >= 21:
    print(f"can go to club with this age --> {age}")
else:
    print(f"can't go to the club with this age --> {age}")

# STEP-4 . Check for the edge cases
 # we should consider edge cases like :
 # -ve ages & extremely high values will break the program
 # Non numeric value like ABU , DF,KFKDFJDSF , will break the program
 # age which ios valid in nature  > 130 not possible

# STEP-5 optimize the logic or code
 # optimization means handling all the edge cases

