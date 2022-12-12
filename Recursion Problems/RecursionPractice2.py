# CAPITALIZE FIRST SOLUTION
def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:]) 

def capitalizeFirst(arr):
    str=[]
    if len(arr)==1:
        str.append(arr[0].capitalize())
    else:
        str.append(arr[0].capitalize())
        str.extend(capitalizeFirst(arr[1:]))
    return str


# NESTED EVEN SUM SOLUTION
def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
    return sum

def nestedEvenSum(obj, sum=0):
    sum=sum
    for i in obj.values():
        if type(i) is int and i%2==0:
            sum+=i 
        if type(i) is dict:
            sum+= nestedEvenSum(i)
    return sum


# CAPITALIZE WORDS SOLUTION
def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])

def capitalizeWords(arr):
    cap=[]
    if len(arr)==1:
        cap.append(arr[0].upper())
    else:
        cap.append(arr[0].upper())
        cap.extend(capitalizeWords(arr[1:]))
    return cap


# STRINGIFY NUMBERS SOLUTION
def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj

def stringifyNumbers(obj):
    d={}
    for i in obj.keys():
        if type(obj[i]) is int:
            d[i]=str(obj[i])
        elif type(obj[i]) is not dict:
            d[i]=obj[i]
        else:
            d[i]=stringifyNumbers(obj[i])
    return d


# COLLECT STRINGS SOLUTION
def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr

def collectStrings(obj):
    s=[]
    for i in obj.values():
        if type(i) is str:
            s.append(i)
        if type(i) is dict:
            s+=collectStrings(i)
    return s

