#This code is written on python 2.7
#'raw_input' on python 2 is identical to 'input' on python 3

a = list('12345')
a = '1 2 3 4 5'
b = a.split()
a = '1:2:3:4:5'
b = a.split(':')
a = '1,2,3,4,5'
b = a.split(',')
a = list(range(10,1,-3))
a.append(4) #append element to the last position
a.extend([2,5])
a.insert(3,0) #index, element
del a[0] #index
a.remove(4) #element


b = a* 2 #keep append elements of 'a' twice
#but with numpy, it doubles the all the elements in 'a'
del(b)
b = []
for x in a:
    b.append(x*2) #doubles all the elements in 'a'
print(b)

#practice p.17

bd = str(input("Input your birthday(yyyymmdd): "))
print(bd[::2])
#from start to end, count of 2, if would be index of 0,2,4,6

#p.18
#list[<start>:<stop>:<step>]
str_ = raw_input("Input string: ")
print(str_[::-1])
#from start to end, count of -1 so, it would be index of -1,-3-5

a = {'name': 'Marry Howard', 'age': 24, 'address':['Fullerton', 'CA', '92831']}
print(a['name'], a['address'])

del a['age'] #key
a.clear()
a = {'name': 'Marry Howard', 'age': 24, 'address':['Fullerton', 'CA', '92831']}
print(a.keys())
print(list(a.keys()))
print(a.values())
print(list(a.values()))

#page 24 practice
n1 = input("Input a first number: ")
n2 = input("Input a second number: ")
Key = str(n1) + 'x' + str(n2)
nm = {Key: []}
nm[Key] = list(range(n1,n1*n2+1, n1))
    
print(nm[Key])


#page 25
import collections 

D = collections.OrderedDict() #disable auto disorder
count = input("Total number of the students: ")
for x in range(0, count):
    ID = raw_input("Student ID: ")
    name = raw_input("Name: ")
    #D[ID] = name
    D.update({ID:name}) #add pair of Key and Value
print("Current dictionary: ")
print(D)

c = 'y'
while (c == 'y' or c == 'Y'):
    s = raw_input("Search ID: ")
    print("Name for the student ID " + s +  " is " + D[s])
    c = raw_input("Continue searching? (y/n)")
  
'''
list vs np.array
operators are literally between list to list,
but elements operations work at np.array.
'''

#page.39

import numpy as np
count = input("Total students: ")
a = np.array([])
for x in range(1, count + 1):
    scores=raw_input(str(x) + ": student's list of scores: ")
    scores = scores.split(",")
    a = np.concatenate((a, np.array(scores)))
    #np.concatenate((arr1, arr2)) -> parameter must be in pair(x,y)
    #axis is meaningless for this code
a = (a.astype(int)).reshape(count,3)

print("GPA: ")
print(a)
print("Sum of GPA for each students: ", np.sum(a, axis = 1))#horizontal
print("Mean of each subjects: ", np.mean(a, axis = 0))#vertical
      
'''
a.ndim #returns dimention
a.shape #returns shape (x,y)
'''






