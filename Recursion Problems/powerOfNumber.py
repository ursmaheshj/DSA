#Finding power/Exponential of a given number

def power(base,exp):
    assert int(exp)==exp,"Exponential must be an integer only"
    if exp ==0:
        return 1
    elif exp<0:
        return 1/base * power(base,exp+1)
    else :
        return base*power(base,exp-1)

print(power(-2,-3))
