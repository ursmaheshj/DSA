#############################################################
#################### One Dimensional Arrays##################
#############################################################

from array import array

#Creation
arr1d=array('i',[4,5,6,8,9])
print('array:',arr1d)

#Insertion
arr1d.insert(1,2)
arr1d.insert(6,5)
print('after insertion:',arr1d)

#Traversal
for i in arr1d:
    print(i)

#Accessing element
def accessElement(arr1d,index):
    if index >= len(arr1d):
        print('Element not present at this index')
    else:
        print(index,':',arr1d[index])

accessElement(arr1d,4)
accessElement(arr1d,12)

#Searching for an element
def searchElement(arr1d,element):
    for i in range(len(arr1d)):
        if arr1d[i]==element:
            return (f'index:{i}')
    return ('Element not found')

print(searchElement(arr1d,6))
print(searchElement(arr1d,10))

#Deleting an element
print('before deletion:',arr1d)
arr1d.remove(4)
arr1d.remove(5)
print('after deletion:',arr1d)


#############################################################
#################### two Dimensional Arrays##################
#############################################################
import numpy as np

#Creation
arr2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,5,2]])
print('2D array',arr2d)

#Insertion
arr2d=np.insert(arr2d,1,[[2,2,2]],axis=1) 
#2nd arg is position and axis denotes col-1 & row-0
print('After insertion',arr2d)

arr2d=np.append(arr2d,[[9,9,9,9,9]],axis=0)
print('After insertion',arr2d)

#Accessing element
def access2DElement(arr,rowInd,colInd):
    if rowInd>=len(arr) or colInd>=len(arr[0]):
        print(f'Element not present @[{rowInd}][{colInd}]')
    else:
        print(f'Element @[{rowInd}][{colInd}] :',arr[rowInd][colInd])

access2DElement(arr2d,4,5)
access2DElement(arr2d,2,1)

#Traversing Array
def traversing2DArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])

traversing2DArray(arr2d)

#Searching element
def search2DElement(arr,value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==value:
                return f'Element is present @ {[i]}{[j]}'
    return f'Element not found @ {[i]}{[j]}'

print(search2DElement(arr2d,5))
print(search2DElement(arr2d,11))

#Deleting element
print('Before deletion','\n',arr2d)
arr2d=np.delete(arr2d,1,axis=0)
print('After deleting 2nd row','\n',arr2d)
arr2d=np.delete(arr2d,0,axis=1)
print('After deleting 1st col','\n',arr2d)