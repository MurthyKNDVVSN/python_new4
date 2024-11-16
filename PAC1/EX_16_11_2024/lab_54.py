for i in range(0,10): # 0 to 9 ,10 times loop will execute
    if i==5:
        print("HI FIVE")
    else:
        print(i)

    # | i | Condition| o/p
    # | 0 | 0 == 5    --> 5 False| o/P --> 0
    # | i | 0 == 5    --> 5 False| o/P --> 1
    # | 2 | 0 == 5    --> 5 False| o/P --> 2
    # | 3 | 0 == 5    --> 5 False| o/P --> 3
    # | 4 | 0 == 5    --> 5 False| o/P --> 4
    # | 5 | 5 == 5    --> 5 true| o/P -->  HI FIVE will be the o/P
    # | 6 | 6 == 5    --> 5 False| o/P --> 6
    # | 7 | 7 == 5    --> 5 False| o/P --> 7
    # | 8 | 8 == 5    --> 5 False| o/P --> 8
    # | 9 | 9 == 5    --> 5 False| o/P --> 9
    # | 10 | 10 == 5   --> 5 False| o/P -->  exit from the loop come out of the loop



