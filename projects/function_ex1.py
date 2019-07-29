"""
Function Exercise 1
    Passing a function as a variable to another function.
Answers by Jennifer Yoon
Date: 1/25/2018 Thursday.
Reference: Joel Grus, Data Science From Scratch, Copyright April 2015, Chp2.

"""

###  Uses functions as passed variables. #########################
def square(x):
    # square of input x.
    print("square", x ** 2 )
    return(x ** 2)

def cube(y):
    # cube of input y.
    print("cube", y ** 3)
    return(y ** 3)

def double(z):
    # double of input z.
    print("double", z * 2)
    return(z * 2)

def passFuncs():
    # Use functions as variables to pass them.
    # print("passFuncs()", square(2), cube(3), double(10))
    return(square(2), cube(3), double(10))

def passFuncs2(x, y, z):
    # Use inputs as parameters for function calls.
    # print("passFuncs2(x, y, z)", square(x), cube(y), double(z))
    return(square(x) + cube(y) + double(z))

result1 = passFuncs()
print("result1", result1)

result2 = passFuncs2(5, 7, 10)
print("result2", result2)

"""     OUTPUTS
>>> result1 = passFuncs()
square 4
cube 27
double 20

>>> print("result1", result1)
result1 (4, 27, 20)


>>> result2 = passFuncs2(5, 7, 10)
square 25
cube 343
double 20

>>> print("result2", result2)
result2 388

"""