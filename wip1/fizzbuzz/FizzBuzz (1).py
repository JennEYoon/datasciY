#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: FizzBuzz test
#-------------------------------------------------------------------------------
def fizzbuzz1():
    for item in range(1,101):
        if item % 15 == 0:
            print "Fizz" + "Buzz"
        elif item % 3 == 0:
            print "Fizz"
        elif item % 5 == 0:
            print "Buzz"
        else:
            print item
##fizzbuzz1()


def fizzbuzz2():
    # Using list.
    # Use + to cancatenate two single list elements.

    z = ["Fizz", "Buzz"]
    for item in range(1,101):
        if item % 15 == 0:
            print z[0] + z[1]
        elif item % 3 == 0:
            print z[0]
        elif item % 5 == 0:
            print z[1]
        else:
            print item
##fizzbuzz2()

def fizzbuzz3():
    # Using a flag variable to test for %3 AND %5 condition.

    for item in range(1,101):
        x = ""
        if item % 3 == 0:
            if item % 5 == 0:
                x = "Buzz"
            print "Fizz" + x
        elif item % 5 == 0:
            print "Buzz"
        else:
            print item
fizzbuzz3()

def fizzbuzz4():
    # Using less if-else statements. Using only 1 print statement.

    for item in range(1,101):
        x = ""
        if item % 3 == 0:
            x = "Fizz"
        if item % 5 == 0:
            x = x + "Buzz"
        if x == "":
            x = item
        print x
##fizzbuzz4()