# Michael Li
# Computers 10
# 5/14/2021
# A chatbot that asks serveral question and responds.
import random
user_response = input("What is your name?")
response_list = ["nice to meet you","good name","great seeing you"]
print("random.choice(response_list)"+ (user_response))
#first question
botinput = input("How is your day?")
response_list2 = ["good to hear", "nice to hear","I hope it would be better"]
print(random.choice(response_list2))
#reply
botinput2 = input("When is your birthday?")
botinput3 = input("Would you invite me to your birthday?")
response_list3 = ["guess what, I won't invite you to my birthday", "I would not be at your birthday anyways"]
print(random.choice(response_list3))
#second question and reply
botquestion4 = input("Am I a robot?")
response_list4 = ["I am a robot", "I am not a robot", "I am human"]
print(random.choice(response_list4))
#third question and reply