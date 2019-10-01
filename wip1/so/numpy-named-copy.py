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
                # Create a dictionary to save all the parts.
                mydict.update({name: b[i,j,k]})
                
    return(mydict)

mydict = {}
result = myfunc(b)
print(result)
# {'arr000': 0, 'arr001': 1, 'arr010': 2, 'arr011': 3, 'arr100': 4, 'arr101': 5, 'arr110': 6, 'arr111': 7}
# You would need to unpack the dictionary to use the arrays separately.
# use "mydict.keys()" to get all array names.
# "for key in keys" to loop through all array names. 