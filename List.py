MyFirstList = [3,45,56,732]
print(MyFirstList)
print(type(MyFirstList))

l2 = ["hello",24,True,55.3]
print(l2)

l3 = ['How are You?',13,MyFirstList]
print(l3)

rng = range(15)
print(rng)

lst = list(range(0,15))
print(lst)

z2 = list(range(100,121))
print(z2)

w = list(range(100,111,2))
print(w)
print("Min in List" , min(w))
print("Max in List" , max(w))


w2 = list(range(100,201,10))
print(w2)




w3 = ['a','b','c','d','e']
#      0   1   2   3   4
#     -5  -4  -3  -2  -1

print(w3[0])
print("Length :" , len(w3))
print("last Element" , w3[-1])

print("3rd Element" , w3[-3])
print("3rd Element" , w3[2])

w3[2] = '63'
print(w3)


#           0     1     2   3     4     5     6    7    8    9
#          -10   -9    -8   -7   -6    -5    -4   -3   -2   -1
letters =  ['A' , 'B', 'C' , 'D' ,'E', 'F', 'G',  'H'  ,'I ','J']
print(letters)
print("lenght of list" , len(letters))


print(letters[:])
print(letters[2:])
print(letters[:7])
print(letters[2:7])

print(letters[-8:7])
print(letters[-8:-3])

#Advanced Slicing
print(letters[2:9:2])
print(letters[::3])


print( "Start from -1 " , letters[::-1])
print( "Start from 2:7:1 " , letters[2:7:1])
print( "Start from 2:7:2 " , letters[2:7:2])

print( "Start from 6:1:-1 " , letters[6:1:-1])   # Always starts negative with left  g,f,e,d,c,b
print( "Start from 6:1:-1 " , letters[6:1:-2])   # Always starts negative with left  g,,e,,c,