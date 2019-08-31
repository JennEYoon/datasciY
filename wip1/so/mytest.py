# testing module, named mytest.py

def test(data, answer):
    if data:
        # If data exists, compare with answer.
        if answer == data * data:
            return "Pass"
        else:
            return "Fail"  

# Call test function.
# result = test(2, 4)
# print(result)            

# result = test(3, 10)
# print(result)     