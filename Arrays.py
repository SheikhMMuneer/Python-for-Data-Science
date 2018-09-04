import numpy as np

l = [23245,27,546,215,-1234]
print(l)


# _pop = l.pop()  # It will remove last element from th list
# print("pop is " ,_pop)
# print(" list after Pop is " ,l)



# To convert list into array of numpy.you can have array of different data types
a = np.array(l)
print("Array ",a)
_mean = a.mean()
print(" Mean = " , _mean)


b = np.array([12,455,63.3,True,"abc"])
print("Array of different data Types:  ",b)

# This will become Array
c = a[2:4]
print("Array c is :" ,c)
print("c[0] :" , c[0])

# This will assign value to Array c
c[:] = 111
print("Array c is :" ,c)
print("Array a is :" ,a)

d = a.copy()
print("Copy of Array is :" ,d)
d[0] = 0
print(d)
print(a)


