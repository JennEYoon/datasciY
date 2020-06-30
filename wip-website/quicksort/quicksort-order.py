#---------------------------------------------------------------------
# Author:      Jennifer Yoon
# File, Path:  module1.py, C:\GDrive\Coding\Python
# Start Time:  06/09/2017  18:00, 6/10 20:00 continue,
# time:        06/11/2017  12:30 pm to 6/12 2 am, 6/12 13:30 continue...
#---------------------------------------------------------------------
import random

xarray = [random.randint(0, 100) for x in range(21)]
orig = xarray[:]
print("L11 random list:", xarray, " length:", len(xarray))
sorted = quicksort(xarray)
print("sorted list:", sorted, " original list:", orig)

def quicksort(xarray):
    print("L16 input to quicksort, xarray:", xarray)
    # Calculate pivot value.
    index = int(len(xarray)/2)
    pivot = xarray[index]
    xarray.pop(index)

    lesser, greater = [], []
    for x in xarray:
       if x < pivot:
            lesser.append(x)
       else:
            greater.append(x)
    left, mid, right = lesser, [pivot], greater
    print("L29 after sort, left, mid, right:", left, mid, right)

    if len(left) > 1 and len(right) > 1:
        print("L32 call left half + right half")
        result = quicksort(left) + mid + quicksort(right)
        print("L34 result of left call + m + right call", result)
    elif len(left) >1:
        print("L36 call left")
        result = quicksort(left) + mid + right
        print("L38 result of left call + M + R", result)
    elif len(right) > 1:
        print("L40 call right")
        result = left + mid + quicksort(right)
        print("L42 result of L + M + right call", result)
    else:
        result = left + mid + right
        print("L45 L+M+R, no calls, base", result)

    print("L47 result before return", result)
    return(result)   # Only one return here.


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

##xarray = [6, 14, 4, 20, 10, 19, 15, 5, 11]
##xarray = [6, 4, 21, 20, 10, 19, 15, 5, 3]
##xarray = [6, 8, 21, 7, 14, 20, 10, 19, 15, 5, 3, 9, 12]
"""