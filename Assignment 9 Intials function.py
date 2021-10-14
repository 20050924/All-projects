#Michael Li
#Computers 10
#2021/6/9
#user types in something then the program prints out the initials of user's response
def initialsfunction(user_response):
    user_response = user_response.upper().strip(".,")
    initials = user_response[0]
    for i in range(len(user_response)):
        if user_response[i] ==" ":
            initials += (user_response[i+1])
    return initials
initials = initialsfunction(input("what is your name"))
print(initials)