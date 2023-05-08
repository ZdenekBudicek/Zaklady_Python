# Local scope a Global scope
student1 = "Harry"


def test():
    student1 = "David"
    print(student1)


test()
print(student1)

# --------------------------------------------------

# Local scope a Global scope
student1 = "Harry"


def test():
    student1 = "David"
    return student1


result = test()
print(result)
