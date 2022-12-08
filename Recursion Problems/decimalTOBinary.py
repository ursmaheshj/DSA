#Conver decimal number to binary form

def DTB(d):
    assert int(d)==d,"Parameter should be integer decimal number"
    if d==0:
        return 0
    return d%2 + 10*DTB(int(d/2))

print(DTB(-12))