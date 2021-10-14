#Michael Li
#Computers 10
#2021/6/10
#Take in a input then output a list of the words form the input.
def splitfunction(user_response):
    user_response = user_response.strip("., ")
    split = []
    a = ""
    for j in range(len(user_response)):
        if user_response[j] !=" ":
            a += user_response[j]
        else:
            split.append(a)
            a = ""
    split.append(a)
    return split
user_response = input("type a sentence")
split = splitfunction(user_response)
print(split)