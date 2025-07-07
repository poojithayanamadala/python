"""
 if
 the python if block is executed when the condition is true
 syntax :
 if condition
    statements
"""
#program
# a=10
# if a==10:
#     print("the if statement is executed.....")

#Accept the number of days from the
#  user and calculate the charge for library according to the following
"""
Till five days : Rs2/day
six to ten : Rs3/day
11 to 15 : Rs4/day
After 15 days: Rs5/day
"""
num = int(input("Enter the days.."))
if num<=5:
    print("The charge is..", num*2)
elif num>=6 and num<=10:
    print("The charge is..", num*3)
elif num>=11 and num<=15:
    print("The charge is..",num*4)
elif num>15:
    print("The charge is..",num*5)
else:
    print("Wrong Days selected..")

"""Write a program to accept two numbers from user and an operator
and perform operation accordingly
num1 : 5
num2 : 10
opr : +
answer : 15
"""
num1 = int(input("enter a number.."))
num2 = int(input("enter a number.."))
opr = input("enter a operator: ")
if opr=="+":
    print("The answer: ", num1+num2)
elif opr=="-":
    print("The answer: ",num1-num2)
elif opr=="*":
    print("The answer: ",num1*num2)
elif opr=="/":
    print("The answer..",num1/num2)
else:
    print("Wrong operator selected..")

    """
Write a program to accept a number from 1 to 12 then 
display name of the month and days in that month
like 1 for january and the no of days 31 and so on
"""
mon_num = int(input("enter the month number 1 to 12.."))
if mon_num==1:
    print("the month is jan it has 31days..")
elif mon_num==2:
    print("the month is feb it has 28days..")
elif mon_num==3:
    print("the month is march it has 31 days..")
elif mon_num==4:
    print("the month is april it has 30 days..")
elif mon_num==5:
    print("the month is may it has 31 days..")
elif mon_num==6:
    print("the month is june it has 30 days..")
elif mon_num==7:
    print("the month is july it has 31 days..")
elif mon_num==8:
    print("the month is August  it has 31 days..")
elif mon_num==9:
    print("the month is september it has 30 days..")
elif mon_num==10:
    print("the month is october  it has 31 days..")
elif mon_num==11:
    print("the month is November  it has 30 days..")
elif mon_num==12:
    print("the month is December  it has 31 days..")
else:
    print("Wrong number ")
"""
Write a program to display "Hello" if a number entered by user
is a multiple of five ottherwise print "Bye"
"""
num = int(input("enter a number.."))
if num%5==0:
    print("hello")
else:
    print("Bye")

"""
Write a Program to display percentages
according to following criteria percentage should accept from user
>90 --> A
>80 and <=90--->B
>60 and <=80 --->C
<=60 --- D
"""
pr = int(input("enter a percentage.."))
if pr>90:
    print("A")
elif pr>80 and pr<=90:
    print("B")
elif pr>60 and pr<=80:
    print("C")
elif pr<=60:
    print("D")
else:
    print("Sorry! Your are Failed..")




i = 1
while i<=10:
    print(i)
i+=1