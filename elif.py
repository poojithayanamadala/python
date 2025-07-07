"""
when the condition in "if" blosk falied elif
block is executed...

syntax:
if condition :
    statements
elif condition:
    statements
else:
    statements
""" 
#checking the userid and password 
userid=input("enter your userid...")
password=input("enter your password...")

if userid=="abc1234"and password=="km@12345":
    print("welcome to our netbanking of kkkkkbank")
elif userid=="jbj34567" and password=="mk@12345":
    print("welcome to our netbankimg of mmmbank")

else:
    print("the userid and password is incorrect..tryagain!!")