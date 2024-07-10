# 1._________pass by value______(immutable objects-strings,integers,floats,tuples)
#def.- when passed immutable objects to function, a copy of the object is created & assigned to alocal variable in function
#    -- any change made to them inside function variable not in outside function.

def addOne(x) :
     x = x+1
     print("Insidde function : ",x)

x = 5
addOne(x)
print("outside function :", x)

# ______pass by reference________
#def.- when passed mutable objects(list,dictionary) to function
#    -- changes inside function will affect the original object.

def modifyList(lst) :
     #lst.append(10)
     lst = [1,5,7,8]
     print("Inside function : ",lst)

lst = [1,2,3,4,5,6]
modifyList(lst)
print("Outside function : ",lst)