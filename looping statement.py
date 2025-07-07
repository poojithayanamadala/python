"""
Looping statements are also called asiterative statements

These statements are used to run a particular condition 
no. of times .... dived into"2"types 
1.while
2.for 
"""

#while: it executes when the condition is true 
"""
syntax: while condition:
           statements
           exit condition/incrementation

#eg:
i=1
while i<=10:
     #print(i)---->in this particular line the 
     #"i" value runs "n" times beacause no incrementation?exit and specified 
     print ("The value", i)
     i+=1


#eg-2:
#while True:
     #print ("the while condition ")
# Note: As default False is given as condition it wont execute 


#eg-3:
#while false:
    #print("the while condition")
#As while is also called entry control 
# loop it just cheecks thecondition in the entrance 
# as default False is given as condition it wont execute
"""
i=0
while i<=10:
       i+=1
       if i==6:
           break#teriminates/stops the program
       print(i)
       

i=0
while i<9:
    i+=1
    if i==3:
        continue
    print(i)