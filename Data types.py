"""
Datatype tells about the type of data that a variable is holding on datatypes are categorised into "5" into
1. number
2. sequence
3.boolean
4.set
5.dictionary
"""
#numbre: which teii about the number datatypes divided into "3" types
"""
integer:which hold all the positive and negative whoie number i.e 0 to n and 0 to -n
integer can be represented as int()
"""
a=123
print(a)
print(type(a))
print(id(a))

"""
type()- which teiis about the type of a value that internally complier holding on
id()-which tells about the address location of a value
"""
a1=-90
print(a1)
print(type(a1))
print(id(a1))

"""
float-which holds all the decimal or fractional values i.e 0 to n.n and 0 to -n.n
it can be represented as float()
"""
b=89.456
print(b)
print(type(b))
print(id(b))

b1=-78.67
print(b1)
print(b1)
print(id(b1))

"""
complex datatype are used to hold the real and imaginary values which can be represented as a+bj
"""
c=78+67j
print(c)
print(type(c))
print(id(c)) 

c1=-456+78j
print(c1)
print(type(c1))
print(id(c1))

""""
sequence datatypes are dividle into "3" types
1.string
2.list
3.tuple
"""

"""
string:it is a collection of/ group of characters 
it can be enclosed using the single quote or quotes 
"""
a="ists"
print(a)
print(type(a))
print(id(a))

b='ists'
print(b)
print(type(b))
print(id(b))

"""
list:it is a collection of items/values/elements
syntax:listname=[val1,val2,....valn]
"""

mylist=[23,45.67,56+89j,"hello"]#item/value/element=4
print(mylist)
print(type(mylist))
print(id(mylist))
print(mylist[2])
print(mylist[3])

"""
in order to acess the element individually we use indexing always start with n-1
syntax to acess the element 
print(listname[elementposition])
"""
"""
tuple is a collection of item /value/element
syntax:tuplename=(val1,val2....valn)
"""
mytuple=(12,23.67,"hi",[1,2,3],(56,78,89))
print(mytuple)
print(type(mytuple))
print(id(mytuple))
print(mytuple[3])

"""
giving a list within a list is called sublist
giving a tuple within a tuple is called sudtuple
"""
"""
boolean:boolean means checks the condition they are divided tu two ways 1.true 2.flase
it can be repressented as bool
"""
a=True
print(a)
print(type(a))

b=False
print(b)
print(type(b))

"""
set:it is coolection of values/items/e'elements
syntax:setname={val1,val2,....valn}
a set cant the list
"""
myset={12,23.34,56+78j,"hi",(45,"hello"),True}
print(myset)
print(type(myset))

"""
dictionary:it is collection of key value pairs
syntax:dictinaryname={key1:val1,key2:val2,...keyn:valn}
"""

mydict={1:"ists","branch":"ece","location":"rjy"}
print(mydict)
print(type(mydict))
