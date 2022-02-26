# minimum operations to get a number N, double or add 1.

def min_op(target,count=0):

    if target==0:
        return count
    if target %2==0:
        count+=1
        return min_op(target/2,count)
    else:
        count+=1
        return min_op((target-1),count)

print(min_op(10))