

"if "
""""
if condition:
    statements

#write a python program to find whether a number is positive or not

num = int(input("enter a number.."))
if num>0:
    print("the number is positive",num)


#write a program to find biggest of two numbers
a = int(input("enter a number: "))
b = int(input("enter a number: "))
if a>b:
    print("A is greater:",a)
else:
    print("B is greater:",b)


#Accept the percentage from the user and display the 
# grade according to the following criteria

BelowD - 25
25 to 45 -- C
45 to 50 -- B
50 to 60--B+
60 to 80--- A
Above 80+--A+


pr = int(input("enter your percentage.."))
if pr<25:
    print("The grade is D..")
elif pr>=25 and pr<=45:
   print("The grade is C..")
elif pr>45 and pr<=50:
    print("The grade is B..")
elif pr>50 and pr<=60:
    print("The grade is B+..")
elif pr>60 and pr<=80:
    print("The grade is A..")
elif pr>80:
    print("The grade is A++..")
else:
    print("Your failed")



#Write a program to diasplay the week names 
# by taking input from user
day = int(input("enter your day.."))
if day==1:
    print("Sunday")
elif day==2:
    print("Monday")
elif day==3:
    print("Tuesday")
elif day==4:
    print("Wednesday")
elif day==5:
    print("Thursday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")

"""

"""
Nested if : A if within a if is called Nested if
syntax: if condition:
               outer if  statements
                if condition:
                    inner if statements
                else:
                    inner else statements       
       else:
            outer else statements
"""
#A Program on Weather Advisories
is_snowing=True
temp=int(input("enter the temperature.."))
if is_snowing>10: #8>10--F
    print("Please carry Umbrella..")
    if is_snowing== -10:
        print("Please carry Umbrella and jacket")
    else:
        print("Enjoy the sunny day!!")
else:
    print("U have a Great Day ")

#Express Delivery
weight=int(input("enter the weight.."))
if weight==4:
    print("the delivery can be expected within 24 hrs..")
    if weight<=10:
        print("Need to pay an extra amount for extra weight..")
    else:
        print("No need to pay any extra charge Have a Great Delivery!!")
else:
    print("Need to wait 3-5 Bussiness days to expect the delivery")

"""
Shorthand if : Writing a if in a line is called shoorthand if
syntax: if condition:  statements
"""
a = 10
if a==10 : print(True)