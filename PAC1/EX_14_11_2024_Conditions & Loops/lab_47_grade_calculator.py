# Grading calculator
# IF Marks b/t 90 to 100 --> print a s grade -a

# logic building
# accept int i/p --> let us say stored it in a variable score
# o/p is string


# Actual logic

SCORE = int(input("ENTER YOUR SCORE:\n"))
if SCORE >= 90 and SCORE <= 100:
    print(" YOUR GRADE IS :", "A")

elif SCORE >= 80 and SCORE <= 89:
    print("YPUR GRADE IS :", "B")

elif SCORE >= 70 and SCORE <= 79:
    print("YOUR GRADE IS :", "C")

elif SCORE >= 60 and SCORE <= 69:
    print("YOUR GRADE IS ", "E")
elif SCORE < 60:
    print("YOUR GRADE IS:", "F")
else:
    if SCORE >= 100 or SCORE <= -1:
        print("YOU ARE SUPER MAN YOU WONT GET A GRADE")
