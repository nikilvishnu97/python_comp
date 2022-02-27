def update_states(arr, start,end):
    # start-=1
    index = start-1
    while index<end:
        print(f"Element at {index} is {arr[index]} and  stateMap is {stateMap[arr[index]]}")
        temp_state = (stateMap[arr[index]]-1)%3
        arr[index]=stateMap[temp_state]
        print(f"updated at {index} is {arr[index]} stateMap is {stateMap[arr[index]]}")
        index+=1
    return arr
def hacking_attempt(arr):
    index = 1
    while index<=N:
        arr = update_states(arr,index,min(N,index+K-1))
        if arr[index-1]=='G':
            index+=1
arr = ['R','Y','G','Y']
stateMap ={'R':2, 'Y':1, 'G':0,0:'G',1:'Y',2:'R'}
N=len(arr)
K=2
hacking_attempt(arr)
print(arr)
