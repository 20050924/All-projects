#Michael Li
#Computers 10
#2021/6/1
#Initials function and self defined split combined
#Initials function = user types in something then the program prints out the initials of user's response
#self defined split = take in a input then output a list of the words form the input
def initialsfunction(user_response):
    user_response = user_response.upper().strip(".,")
    initials = user_response[0]
    for i in range(len(user_response)):
        if user_response[i] ==" ":
            initials += (user_response[i+1])
    return initials
def splitfunction(user_response2):
    user_response2 = user_response2.strip(".,")
    split = []
    a = ""
    for j in range(len(user_response2)):
        if user_response2[j] !=" ":
            a += user_response2[j]
        else:
            split.append(a)
            a = ""
    split.append(a)
    return split
def main():
    user_response = input("type your name")
    initials = initialsfunction(user_response)
    user_response2 = input (f"Hi {initials}, type a sentence")
    split = splitfunction(user_response2)
    print(f"Here is your sentence in a list{split}")
main()