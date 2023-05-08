# Vytvoření globální proměnná
def test():
    global my_name
    my_name = "Harry"
    print(my_name)
    return my_name


result = test()
print(my_name)
print(result)
