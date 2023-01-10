from array import array

#Creation
arr=array('i',[4,5,6,8,9])
print('array:',arr)

#Insertion
arr.insert(1,2)
arr.insert(6,5)
print('after insertion:',arr)

#Traversal
for i in arr:
    print(i)

#Accessing element
def accessElement(arr,index):
    if index >= len(arr):
        print('Element not present at this index')
    else:
        print(index,':',arr[index])

accessElement(arr,4)
accessElement(arr,12)

#Searching for an element
def searchElement(arr,element):
    for i in range(len(arr)):
        if arr[i]==element:
            return (f'index:{i}')
    return ('Element not found')

print(searchElement(arr,6))
print(searchElement(arr,10))

#Deleting an element
arr.remove(4)
print('before deletion:',arr)
arr.remove(5)
print('after deletion:',arr)
