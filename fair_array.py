import sys


arr = "2,8,14,20,10,15"
arr = list(map(int,arr.split(",")))
print(arr)


def fair(arr):
    arr = sorted(arr)
    return min([abs(arr[j+1]-arr[j]) for j in range(len(arr)-1)])
print(fair(arr))

