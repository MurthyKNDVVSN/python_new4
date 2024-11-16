for i in range(1, 10, 1):
    if i == 6 or i == 5:
        print(i)
    else:
        pass  # pass is place holder stmt tat does nothing
              # It's used when a stmt is syntactically required but no action is needed
    # | i | Condition| o/p
    # | 0 | 0 == 6    -->  False| o/P --> Nothing will be printed
    # | i | 1 == 6    -->  False| o/P --> Nothing will be printed
    # | 2 | 2 == 6    -->  False| o/P --> Nothing will be printed
    # | 3 | 3 == 6    -->  False| o/P --> Nothing will be printed
    # | 4 | 4 == 6    -->  False| o/P --> Nothing will be printed
    # | 5 | 5 == 6    -->  true| o/P  --> 5
    # | 3 | 6 == 6    -->  TRUE| o/P -->  6
    # | 4 | 7 == 6    -->  False| o/P --> Nothing will be printed
    # | 5 | 8 == 6    -->  true| o/P  --> Nothing will be printed
    # | 4 | 9 == 6    -->  False| o/P --> Nothing will be printed
    # | 4 | 10 == 6    -->  False| o/P --> for loop finished and comes out of the loop
