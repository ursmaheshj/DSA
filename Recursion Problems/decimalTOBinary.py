#Conver decimal number to binary form

def DTB(d):
    if d==0:
        return '0'
    elif d==1 :
        return '1'
    else:
        if d%2==0:
            return str(DTB(d//2))+str(0)
        else:
            return str(DTB(d//2))+str(1)

print(DTB(456))