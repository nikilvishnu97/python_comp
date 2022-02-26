

from numpy import math

def find_position(array,num):
    copy_arr = array
    mid = array.index(num) if num in array else -1
    if mid<0:
        while len(copy_arr)>1 :
            print(copy_arr)
            mid = int(len(copy_arr)/2)
            if num<copy_arr[mid]:
                copy_arr = copy_arr[:mid]
            else:
                copy_arr = copy_arr[mid:]
    else:
        return array[mid-1],array[mid+1]
    mid = array.index(copy_arr[0])
    if mid<len(array)-1 and mid>0:
        return array[mid-1],array[mid+1]
    elif mid>1:
        return array[mid+1]
    else:
        return array[mid-1]

    


print(find_position([1,4,6,8,9],5))