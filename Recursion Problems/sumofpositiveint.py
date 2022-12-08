#Find sum of n positive numbers

def sumofpositivenumbers(n):
    assert n>=0 and int(n)==n, "Provide a positive integer only"
    if n==0:
        return 0
    else:
        return (n%10)+sumofpositivenumbers(n//10)

print(sumofpositivenumbers(15451))
