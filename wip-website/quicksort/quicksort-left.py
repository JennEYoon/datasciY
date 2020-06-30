"""doc string
#---------------------------------------------------------------------
# Author:      Jennifer Yoon
# File, Path:  module1.py, C:\GDrive\Coding\Python
# Start Time:  06/09/2017  18:00
# time:        06/10/2017  20:00 continue
#---------------------------------------------------------------------

0) create random list.
1) pick middle pivot, index, value.
2) full list -- compare with pivot value, attach to left or right.
3) reassemble left + pivot + right, return up the tree.
4) left section, recursive call
5) right section, recursive call
6) reassemble sub-array, left + pivot + right.
7) stop if length of sub-section is 0.
8) if length == 1, don't sort, just assemble.
"""

##import random

#  Randomly generate a list of integers.
##xarray = [random.randint(0, 21) for x in range(9)]
##print("random list ", xarray, "length ", len(xarray))
##orig = xarray

def quicksort(xarray):

    # Calculate pivot value.
    index = int(len(xarray)/2)
    pivot = xarray[index]
    xarray.pop(index)
    print("quicksort beginning: ", pivot, xarray)

    lesser, greater = [], []
    for x in xarray:
       if x < pivot:
            lesser.append(x)
       else:
            greater.append(x)
    print("quicksort middle: ", lesser, pivot, greater)

    # after quick sort - rember partial results.
    left = lesser
    mid = [pivot]
    right = greater
    print("partial results to memory: ", left, mid, right)

    stop = False
    if stop == False and len(left) > 1:
        result = quicksort(left)
        return(result + mid + right)
    else:
        return(left + mid + right)
        stop = True

xarray = [6, 4, 21, 20, 10, 19, 15, 5, 3]
orig = xarray[:]

result = quicksort(xarray)
print("sorted list", result, " original list", orig)


###  First call to split original array into less and greater lists.
##print("First gen call to split list. --------------------")
##less, greater = [], []
##quicksort(xarray, pivot)
##print(less, greater, "pivot", pivot)
##xarray2 = less
##xarray3 = greater
##
### Second call less-half.
##print("Second gen left-half call to re-split list.---------")
##pivot2 = xarray2[int(len(xarray2)/2)-1]
##less, greater = [], []
##quicksort(xarray2, pivot2)
##print(less, greater, "pivot", pivot2)
##
##xarray4 = less
##xarray5 = greater
##
### Second call greater-half.
##print("Second gen right-half call to re-split list.-------")
##pivot3 = xarray3[int(len(xarray3)/2)]
##less, greater = [], []
##quicksort(xarray3, pivot3)
##print(less, greater, "pivot", pivot3)
##
##xarray6 = less
##xarray7 = greater
##
### Tree-binary calls there after.
##less, greater = [], []
