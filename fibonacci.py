#To find out the fibonnaci number at given position

def fibonacci(n):
    assert n>=0 and int(n)==n,"Fibonnaci can't be negative or non-integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        

print(fibonacci(6))
