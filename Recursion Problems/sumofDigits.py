#Find sum of Digits of given positive number

def sumofDigits(n):
    assert n>=0 and int(n)==n, "Provide a positive number only"
    if n==0:
        return 0
    else:
        return (n%10)+sumofDigits(n//10)

print(sumofDigits(15451))
