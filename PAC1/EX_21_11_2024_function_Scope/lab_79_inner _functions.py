def outer_function():
    var1 = 30 # local

    def inner_function():
        var2 = 90
        print(var1)

    def inner_function2():
        print(var1)

    inner_function()
    inner_function2()
    #print(var2) this one we can't print or we can't use it in inner_function2()

outer_function()
# inner_function()