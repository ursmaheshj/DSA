#Lists creation
myList = [1,2.5,'a',[3,'Mahesh']]
print('List:',myList)

#Traversing list
for i in myList:
    print(i)

#Inserting/updating
print('Before insert/update:',myList)

myList.insert(1,5)
print('After insert:',myList)

myList.append('at end')
print('After append:',myList)

myList.extend('abc')
myList.extend([1,2,3])
print('After extend:',myList)

# Accessing Element
print(myList[4])
print(myList[5:9])

#Searching an element
def searchElement(list,value):
    if value in list:
        print('Exist')
    else:
        print('Not found')

searchElement(myList,'Mahesh')
searchElement(myList,2)

#Deleting an element
print('Before Deletion:',myList)

myList.pop(1)   ##takes index as argument
print('After pop:',myList)

myList.pop()
print('After pop:',myList)

myList.remove('a')    ##takes value as argument
print('After remove:',myList)

del myList[1:4]
print('After del:',myList)