#Finding greatest common divisor of two numbers.

def GCD(a,b):
    assert int(a)==a and int(b)==b,"Numbers must be integers only."
    if 0 in [a,b]:
        return max(a,b)
    if a>b:
        return GCD(a//b,a%b)
    else:
        return GCD(b//a,b%a)

print(GCD(8,-12))