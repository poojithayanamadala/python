"""
logical oparators are useb to perform logical operations they are logical and,or,not
And--if both the condtions are ture it retruns the true
T T T
F T F
T F F
F F F
Or--if one of the condition is true it retruns the true
T F T
F T T 
F F F
Not-- it just negotiates the condition
 T F
 F T
"""
a=13
b=45
c=a>=34 and b<=50
print(c)

d=67
e=89
f=d!=67 or e==89
print(f)

a=10
print(not(a))#f

b=0
print(not(b))#t