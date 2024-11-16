for i in range(0, 10):  # 0 to 9 ,10 times loop will execute
    print(i)
    if i == 5:
        break

    # | i | Condition| o/p
    # | 0 | 0 == 5    --> 5 False| o/P --> 0
    # | i | 0 == 5    --> 5 False| o/P --> 1
    # | 2 | 0 == 5    --> 5 False| o/P --> 2
    # | 3 | 0 == 5    --> 5 False| o/P --> 3
    # | 4 | 0 == 5    --> 5 False| o/P --> 4
    # | 5 | 5 == 5    --> 5 true| o/P -->  Breaks the loop and come out of the loop
