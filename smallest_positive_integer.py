def smallest_int(a):
    small = 99999
    mapObj = {}
    for val in a:
        if val>0 and val<small:
            mapObj[val] = True;
            small = val
    index = 1
    while index < small:
        if index not in mapObj:
            return index
        index+=1

print(smallest_int([-5, 2, 0, -1, -10, 15]))