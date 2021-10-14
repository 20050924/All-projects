#Michael Li
#Programming 11
#2021/9/9
#Assignment 13, A password systeam that remember user's username, password and able to Create new username and password

import json
import random
file = open("passwordsystem.txt","r")
x = file.readline()
user_dictionary = json.loads(x)
upper_password = False
int_password = False
punctuation_password = False
#strings for checking user's password have met requirements or not.
symboles = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","{","]","}","|",";",":","'",'"',",",".","/","<",">","?"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
upper_case = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
lower_case = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
random_password = []
#list for creating a random password
print("please enter your username or done to end program")
user_response = input()
user_dictionary.get(user_response)
if user_response in user_dictionary:
    print("please enter your password(done)")
    while True:
        password_response = input()
        if password_response == (user_dictionary.get(user_response)):
            print("Password correct, program end")
            exit()
        elif password_response == "done":
            exit()
        elif password_response != (user_dictionary.get(user_response)):
            print("invalid password, please try agian")
elif user_response == "done":
    exit()
#when user typed a correct username, system tells user to type password and check if the password is correct.
elif user_response != user_dictionary:
    print("invalid username, creating new account. Would you like to have a own password or have the system generate a random password.(own/system/done)")
    create_account_response = input()
    if create_account_response == "own":
        print("Enter your password, your password must be at least 8 characters and have at least 1 upper-case letter, 1 number, and 1 punctuation symbole.(done)")
        while True:
            own_password = input()
            for i in range(len(own_password)):
                if str.isupper(own_password[i]) == True:
                    upper_password = True
                elif (own_password[i]) in numbers:
                    int_password = True
                elif own_password[i] in symboles:
                    punctuation_password = True
            if len(own_password)>=8 and upper_password == True and int_password == True and punctuation_password == True : 
                user_dictionary[user_response] = own_password
                json_dictionary = json.dumps(user_dictionary)
                file= open("passwordsystem.txt","w")
                file.write(json_dictionary)
                file.close()
                print(f"your username is {user_response} your password is {own_password}")
                print("username and password recorded, program end")
                break
#writing username and password in to program
            elif own_password == "done":
                exit()
            elif len(own_password)<=8 or upper_password != True or int_password != True or punctuation_password != True :
                print("invalid password, your password must be at least 8 characters and have at least 1 upper-case letter, 1 number, and 1 punctuation symbole.(done)")
#when user typed a invalid username and choose to write their own password program will check if his password met requirement.
    elif create_account_response == "done":
        exit()
    elif create_account_response == "system":
        while True:    
            print("how many characters?")
            password_character = int(input())
            break
        while password_character <8:
            print("password need to have atleast 8 characters")
            print("how many characters?")
            password_character = int(input())
        while True:
            print("how many upper case?")
            password_uppercase = int(input())
            break
        while password_uppercase < 1:
            print("password need to have atleast 1 uppercase")
            print("how many upper case?")
            password_uppercase = int(input())
        while True:
            print("how many numbers?")
            password_numbers = int(input())
            break
        while password_numbers <1:
            print("password need to have atleast 1 numbers")
            print("how many numbers?")
            password_numbers = int(input())
        while True:
            print("how many punctuation symboles?")
            password_symboles = int(input())
            break
        while password_symboles < 1:
            print("password need to have atleast 1 symboles")
            print("how many punctuation symboles?")
            password_symboles = int(input())
        if password_uppercase+password_numbers+password_symboles > password_character:
            print("you can't have uppercases, numbers and symboles add up together be more than the characters. Program end")
            exit()
    
        for i in range(password_uppercase):
            random_password.append(random.choice(upper_case))
        for i in range(password_numbers):
            random_password.append(random.choice(numbers))
        for i in range(password_symboles):
            random_password.append(random.choice(symboles))
        while True:
            random_password.append(random.choice(lower_case))
            if len(random_password) == password_character:
                break
#If user wants system to generate a password. A bunch of While loop will create a random password and ask user how many character,symbols,numbers they want
        random.shuffle(random_password)
        system_password = "".join(random_password)
        user_dictionary[user_response] = system_password
        json_dictionary = json.dumps(user_dictionary)
        file= open("passwordsystem.txt","w")
        file.write(json_dictionary)
        file.close()
        print(f"your username is {user_response} your password is {system_password}")
        print("username and password recorded, program end")
#writes system password in to system