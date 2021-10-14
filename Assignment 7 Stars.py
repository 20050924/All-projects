#Michael Li
#Computers 10
#2021/6/3
#Based on the number user given to the bot, the bot response to you with stars.

user_response = input("type a number")
for i in range (int(user_response)):
    a = "*"
    for b in range (i):
        a +="*"
    print (a)