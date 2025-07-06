"""
Identity operators are used to compare the value and return the boolean values..
the operators are "is","is not"
"""
x=[1,2,3]
y=[4,5,6]
z=x
print(x is y)#f
print(x is z)#t
print(y is z)#f
print(y is not z)#t
print(z is not x)#f
print(x is not y)#t