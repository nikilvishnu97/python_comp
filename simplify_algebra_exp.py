#Incomplete but solution is similar, just if else loop changes
def simplify(exp):
    print()
    replace_char = False
    for index,value in enumerate(exp):
        if value == "-":
            if exp[index+1]=="(":
                replace_char = True
                continue
        if replace_char:
            if value =="+":
                exp = exp[:index]+"-"+exp[index+1:]
            elif value =="-":
                exp = exp[:index]+"+"+exp[index+1:]
        if value ==")":
            replace_char = False
    print(exp)

simplify("a-(b-c-(d+e))-f")