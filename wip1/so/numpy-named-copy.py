import numpy as np

b = np.array([0, 1, 2, 3, 4, 5, 6, 7])
b = np.reshape(b, (2, 2, 2))
print(b, type(b))

def myfunc(arr):
    for i in range(b.shape[0]):
        for j in range(b.shape[1]):
            for k in range(b.shape[2]):
                # Create a new array name from string parts.
                name = "arr"+str(i)+str(j)+str(k)
                print(name, b[i, j, k])
                # Add a new key-value pair to the dictionary.
                mydict.update({name: b[i,j,k]})
    return(mydict)

mydict = {}
result = myfunc(b)
print(result)
# {'arr000': 0, 'arr001': 1, 'arr010': 2, 'arr011': 3, 'arr100': 4, 'arr101': 5, 'arr110': 6, 'arr111': 7}
# You would need to unpack the dictionary to use the arrays separately.
# use "mydict.keys()" to get all array names.
# "for key in keys" to loop through all array names. 
# mydict['arr000'] will return the value 0.

"""
Your question tags "numpy" but does not use it in your code snippet. If you are trying to stick with numpy, there is another method called "structured data array". It's similar to a dictionary in that "name" and "value" can be stored as paired sets in a numpy array. This keeps numpy's efficient memory management and fast calculation (C optimization). This matters if you are working with large datasets.

Also if working with numpy, there may be a way to use its index attribute in a variable name.

Later, I will think of examples for both and update my answer if possible.
"""
