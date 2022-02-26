from xmlrpc.client import MAXINT


def max_sum_fun_adj(array):
    max_sum = -MAXINT-1
    max_sum_loop = 0
    for i in array:
        max_sum_loop +=i
        max_sum = max(max_sum,max_sum_loop)
        if max_sum_loop<0:
            max_sum_loop = 0
    return max_sum
print(max_sum_fun_adj([-2,1,3,-4,5,6,3,-11,10,5,6,-10]))

def max_sum_non_Adj(array):
    max_sum = 0
    previous_max = 0
    for index in array:
        previous_max = max(max_sum,previous_max)
        max_sum+=index
    return max(previous_max,max_sum)
print(max_sum_non_Adj([-2,1,3,-4,5,6,3,-11,10,5,6,-10]))
        
