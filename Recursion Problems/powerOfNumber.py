#Finding power/Exponential of a given number

def power(base,exp):
    assert exp>=0 and int(exp)==exp,"Exponential must be an positive integer only"
    if exp ==0:
        return 1
    else :
        return base*power(base,exp-1)

print(power(-3,-3))