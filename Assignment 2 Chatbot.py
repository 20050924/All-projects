#Michael Li
#Computers 10
#2021/5/18
#A chatbot that plays a game with user and able to response to what user said.

import random
user_response = ""
user_response2 = ""
respond_list = ["You didn't follow my instructions properly", "You've done something wrong", "You are lying, the ring has no chance to be on 1 or 5, please follow instructions properly."] 
respond_list2 = ["Thanks for your time with me", "THE END"]

print("Lets play a game. (Press enter or type something to continue)")
input()
print("First reach out your right hand and give your five fingers a number. You can either use the order 12345 or 54321")
input()
print("Now, imagine a invisible ring on one of your fingers and you can decide which finger the ring is on.")
input()
print("Next, you will move your ring to another finger. You can only move it to the finger next it. For example, if your ring is on 4, you can only move it to 3 or 5, not 1 or 2 if your ring is on 5 you can only move it to 4 and not 1, 2, or 3. Now move your ring five times.")
input()
print("Now figure out what number your ring is on, and move your ring the same number of times. For example, if your ring is on 2, move it 2 times.")
input()
#this is all bot telling the rules of the game
while True:
    print("Your ring is not on 1 or 5. Am I right?")
    user_response = input()
    if user_response == "Yes" or user_response == "yes":
        print("That is what I thought. Now move the ring 3 times, while the ring can't go to 1 and 5.")
        print("Put your fighers that doesn't have the ring on away.")
        print("Why are you pointing your middle finger at me?")
        while True:
            print("Do you want to know how this works?")
            user_response2 = input()
            if user_response2 == "yes" or user_response2 == "Yes":
                print("The first step is to move the ring 5 times which doesn't matter it can be on 12345, the next step is to move the ring the number that represents what finger it is on times, odd number(135) moves odd number of times would be a even number(24) and even number moves even number of times would still be even, so after this step the ring can only be on even number(24), and 24 moves 3 time would only moves to 3 which is the middle finger")
                print(random.choice(respond_list2))
                break
            elif user_response2 == "No" or user_response2 == "no":
                print(random.choice(respond_list2))
                break
            else:
                print("I'm sorry, I didn't understand what you said. please say Yes or No")
        break
    elif user_response == "No" or user_response == "no":
        print(random.choice(respond_list))
        print("If you really don't understand how it works type yes to get how this thing works")
    else:
        print("I'm sorry, I didn't understand what you said, please say Yes or No")


