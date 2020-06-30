#---------------------------------------------------------------------
# Author:      Jennifer Yoon
# File, Path:  module1.py, C:\GDrive\Coding\Python
# Start Time:  06/09/2017  18:00
# time:        06/10/2017  20:00 continue
# time:        06/12/2017  00:27 -- started 12:30pm on 6/11.
#---------------------------------------------------------------------

def quicksort(xarray):

    # Calculate pivot value.
    index = int(len(xarray)/2)
    pivot = xarray[index]
    xarray.pop(index)
    print("quicksort beginning, pivot, xarray: ", pivot, xarray)

    lesser, greater = [], []
    for x in xarray:
       if x < pivot:
            lesser.append(x)
       else:
            greater.append(x)
    print("quicksort middle, lesser, pivot, greater: ", lesser, pivot, greater)

    # after quick sort - rember partial results.
    left = lesser
    mid = [pivot]
    right = greater
    print("partial results to memory L, M, R: ", left, mid, right)

    if len(left) > 1 and len(right) > 1:
        print("call left half + right half")
        result = quicksort(left) + mid + quicksort(right)
        print("result of left call + m + right call", result)
    elif len(left) >1:
        print("call left")
        result = quicksort(left) + mid + right
        print("result of left call + M + R", result)
    elif len(right) > 1:
        print("call right")
        result = left + mid + quicksort(right)
        print("result of L + M + right call", result)
    else:
        result = left + mid + right
        print("L+M+R, no calls, base", result)

    print("result before return", result)
    return(result)
    # Only one return here.
    # Later, return after each call to quicksort. No, not needed!!!

xarray = [6, 14, 4, 20, 10, 19, 15, 5, 11]
orig = xarray[:]
sorted = quicksort(xarray)
print("sorted list", sorted, " original list", orig)


""" notes:
0) create random list.
1) pick middle pivot, index, value.
2) full list -- compare with pivot value, attach to left or right.
3) reassemble left + pivot + right, return up the tree.
4) left section, recursive call
5) right section, recursive call
6) reassemble sub-array, left + pivot + right.
7) stop if length of sub-section is 0.
8) if length == 1, don't sort, just assemble.


##xarray = [6, 4, 21, 20, 10, 19, 15, 5, 3]
##xarray = [6, 8, 21, 7, 14, 20, 10, 19, 15, 5, 3, 9, 12]

##import random
##xarray = [random.randint(0, 21) for x in range(9)]
##print("random list ", xarray, "length ", len(xarray))
"""