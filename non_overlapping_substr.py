factorialMap = {}
def factorial(n):
    if n in factorialMap:
        return factorialMap[n]
    if n<2:
        return 1
    factorialMap[n]=n*factorial(n-1) 
    return factorialMap[n]

# print(factorial(10))
# print(factorialMap)
def non_overallapping(inputStr):
    comb = 0
    n = len(inputStr)
    print(2**(len(inputStr)-1))
    for index in range(n):
        comb += int(factorial(n)/(factorial(n-index)*factorial(index)))
    return comb
print(non_overallapping("ABCD"))
