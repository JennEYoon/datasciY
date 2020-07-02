# Swap A with B without using a 3rd temp location.

def swap1():
    a = 5
    b = 3
    print a, b
    a, b = b, a
    print a, b
##swap1()

def swap2():
    a = "Fizz"
    b = "Buzz"
    print a, b
    a, b = b, a
    print a, b
##swap2()

def swap3():
    a = 5
    b = 15
    print a, b
    b = b + a
    a = b - a
    b = b - a
    print a, b
##swap3()

def swap4():
    # String with fixed length, 5 characters each.
    a = "Hello"
    b = "World"
    print a, b
    b = b + a
    a = b[0:5] # first 5 characters, 0 to 4.
    b = b[5:10] # last 5 characters, 5 to 9.
    print a, b
##swap4()

def swap5():
    # switch assigment order of a and b.
    # character lenght unknown.
    a = "Mary"
    b = "Jonathan"
    alen = len(a)
    print a, b
    a += b         # a becomes combo in a-b order.
    b = a[ :alen]  # b becomes first half of combo, old a.
    a = a[alen: ]  # a become second half of combo, old b.
    print a, b
##swap5()