def distance_between_duplicates(arr):
    visited_map={}
    final_arr = []
    for index,ele in enumerate(arr):
        if ele not in visited_map:
            visited_map[ele]=index
        else:
            final_arr.append(index-visited_map[ele])
    return max(final_arr)


print(distance_between_duplicates([3,2,1,2,1,4,5,8,6,7,4,2]))