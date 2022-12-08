#Finding greatest common divisor of two numbers.

def GCD(a,b):
    assert int(a)==a and int(b)==b,"Numbers must be integers only."
    if a<0:
        a=-a
    if b<0:
        b=-b
    if b==0:
        return a
    else:
        return GCD(b,a%b)

print(GCD(18,48))