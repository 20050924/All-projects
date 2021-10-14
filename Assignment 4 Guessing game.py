#Michael Li
#Computers 10
#2021/5/25
#This is a two player guessing game that the bot gives a topic player 1 types a word related to the topic, then player 2 look at the topic and have 3 chances to guess player 1's word.
import random
topic_list = ["school","family","computer","internet","human", "robot", "tree","numbers between 1 to 5","planet","students","culture","country","microsoft","apple","fruit","foods","sky","colour","ocean","animals","birds","buildings"]
topic = ""
user_response = ""
user_response2 = ""
#player 1 response
user_response3 = ""
#player 2 response



print("This is a game that the program give User1 a topic. User1 will enter a word related to the topic. Then the program will tell User2 the topic and User2 will have 3 tries to gusee User 1's word(type start to start the game)")
#rules
while True:
    user_response = input()
#game start when they type start
    user_response = user_response.lower().strip(" ,.")
    if user_response == "start":
        topic = random.choice(topic_list)
        print("the topic is:", topic)
        print("type a word related to the topic")
        user_response2 = input()
        user_response2 = user_response2.lower().strip(" ,.")
        break
    else:
        print("sorry, I don't understand, please type start")
print("\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n""\n","\n","\n")
#player 1 give a word related to topic
print("the topic is:", topic)
for i in range(3):
    user_response3 = input()
    user_response3 = user_response3.lower().strip(" ,.")
    if user_response3 == user_response2:
        print("congrats,you are correct")
        break
    else:
        print("You guessed the wrong answer")
#checks player2 answer and give 3 tries
print("Player 1's word is", user_response2)
