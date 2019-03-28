"""
Function Exercise 1
    A) Looping test.
    B) Passing a function as a variable to another function.
Answers by Jennifer Yoon
Date: 1/25/2018 Thursday.
Reference: Joel Grus, Data Science From Scratch, Copyright April 2015, Chp2.

"""


### Looping, for i in range(x):  ##########################
def loop():
    for i in [1, 2, 3, 4, 5]:
        print(i+i)
        for j in [6, 7, 8, 9, 10]:
            print(j)
            print(i, j)
        print("next", i)
    print("done")
# Calls loop function.  Testing of interating through a list.
loop()

"""     OUTPUTS
>>> loop()
2
6
1 6
7
1 7
8
1 8
9
1 9
10
1 10
next 1
4
6
2 6
7
2 7
8
2 8
9
2 9
10
2 10
next 2
6
6
3 6
7
3 7
8
3 8
9
3 9
10
3 10
next 3
8
6
4 6
7
4 7
8
4 8
9
4 9
10
4 10
next 4
10
6
5 6
7
5 7
8
5 8
9
5 9
10
5 10
next 5
done
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

