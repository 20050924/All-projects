#Michael Li
#Programming 11
#2021/10/5
#Assignment 18, A tic tac toe game program that player aginst Ai.
#Ai smarter(can place a X when ai is able to win)
#have a bug when game ends it pops out a error(don't know how to fix: Internal error: bunch of codes file name etc and then OSError: [Errno 22] Invalid argument)
from tkinter import *
import random
root = Tk()
canvas = Canvas(root, height=666, width=666)
canvas.pack()
gamestate = ["","","","","","","","",""]
print("click on a square and will create a circle there")
print("Contians 3 circle's horizontaly,verticaly and oblique wins game, same with the computer")
def O(event):
    global gamestate
    if event.x <= 222 and event.y <= 222 and gamestate[0] == "" :
        canvas.create_oval(22,22,200,200 ,width = 5)
        gamestate[0] = "O"
        X()
    elif event.x <= 444 and event.x >222 and event.y <= 222 and gamestate[1] == "":
        canvas.create_oval(242,22,422,200 ,width = 5)
        gamestate[1] = "O"
        X()
    elif event.x <=666 and event.x > 444 and event.y <= 222 and gamestate[2] == "":
        canvas.create_oval(464,22,644,200,width=5)
        gamestate[2] = "O"
        X()
    elif event.x<= 222 and event.y > 222 and event.y <=444 and gamestate[3] == "":
        canvas.create_oval(22,244,200,422,width=5)
        gamestate[3] = "O"
        X()
    elif event.x<= 444 and event.x >222 and event.y>222 and event.y <= 444 and gamestate[4] == "":
        canvas.create_oval(244,244,422,422,width=5)
        gamestate[4] = "O"
        X()
    elif event.x <=666 and event.x> 444 and event.y >222 and event.y <=444 and gamestate[5] == "":
        canvas.create_oval(466,244,644,422,width=5)
        gamestate[5] = "O"
        X()
    elif event.x <=222 and event.y >444 and event.y <=666 and gamestate[6] == "":
        canvas.create_oval(22,466,200,644,width=5)
        gamestate[6] = "O"
        X()
    elif event.x>222 and event.x<=444 and event.y >444 and event.y <=666 and gamestate[7] == "":
        canvas.create_oval(244,466,422,644,width=5)
        gamestate[7] = "O"
        X()
    elif event.x > 444 and event.x <666 and event.y>444 and event.y <=666 and gamestate[8] == "":
        canvas.create_oval(466,466,644,644,width=5)
        gamestate[8]= "O"
        X()
#player clicked mouse and create a O on what ever square they click. 
    if gamestate[0] == "O" and gamestate[1] == "O" and gamestate[2] == "O":
        print("Player win, game end")
        exit()
    elif gamestate[0] == "O" and gamestate[3] == "O" and gamestate[6] == "O":
        print("Player win,game end")
        exit()
    elif gamestate[0] == "O" and gamestate[4] == "O" and  gamestate[8] == "O":
        print("Player win,game end")
        exit()
    elif gamestate[1] == "O" and gamestate[4] == "O" and gamestate [7] == "O":
        print("Player win,game end")
        exit()
    elif gamestate[2] == "O" and gamestate[5] == "O"  and gamestate[8]== "O":
        print("Player win,game end")
        exit()
    elif gamestate[2] == "O" and gamestate [4] == "O" and  gamestate[6]== "O":
        print("Player win,game end")
        exit()
    elif gamestate[3] == "O" and gamestate [4] == "O" and  gamestate[5]== "O":
        print("Player win,game end")
        exit()
    elif gamestate[6] == "O" and gamestate [7] == "O" and  gamestate[8]== "O":
        print("Player win,game end")
        exit()
    elif gamestate[0] != "" and gamestate[1] != "" and gamestate[2] != "" and gamestate[3] != "" and gamestate[4] != ""and gamestate[5] != ""and gamestate[6] != ""and gamestate[7] != ""and gamestate[8] != "":
        print("Tie,game end")
        exit()
#check if player wins
def createX1():
    canvas.create_line(22,22,200,200 ,width = 5)
    canvas.create_line(200,22,22,200 ,width = 5)
    gamestate[0] = "X"
def createX2():
    canvas.create_line(244,22,422,200 ,width = 5)
    canvas.create_line(422,22,244,200 ,width = 5)
    gamestate[1]="X"
def createX3():
    canvas.create_line(466,22,644,200,width=5)
    canvas.create_line(644,22,466,200,width=5)
    gamestate[2]="X"
def createX4():
    canvas.create_line(22,244,200,422,width=5)
    canvas.create_line(200,244,22,422,width=5)
    gamestate[3]="X"
def createX5():
    canvas.create_line(244,244,422,422,width=5)
    canvas.create_line(422,244,244,422,width=5)
    gamestate[4]="X"
def createX6():
    canvas.create_line(466,244,644,422,width=5)
    canvas.create_line(644,244,466,422,width=5)
    gamestate[5]="X"
def createX7():
    canvas.create_line(22,466,200,644,width=5)
    canvas.create_line(200,466,22,644,width=5)
    gamestate[6]="X"
def createX8():
    canvas.create_line(244,466,422,644,width=5)
    canvas.create_line(422,466,244,644,width=5)
    gamestate[7]="X"
def createX9():
    canvas.create_line(466,466,644,644,width=5)
    canvas.create_line(644,466,466,644,width=5)
    gamestate[8]="X"
#funtions to create X
def X():
    global gamestate
    while True:
        random_int = random.randint(0,8)
        if  gamestate[6] == "X" and gamestate[3] == "X" and gamestate[0] == "":
            createX1()
            break
        elif gamestate[2]=="X" and gamestate[1]=="X" and gamestate[0] == "":
            createX1()
            break
        elif gamestate[4]=="X" and gamestate[8]=="X" and gamestate[0] == "":
            createX1()
            break
        elif gamestate[0]=="X" and gamestate[2]=="X" and gamestate[1] == "":
            createX2()
            break
        elif gamestate[4]=="X" and gamestate[7]=="X" and gamestate[1] == "":
            createX2()
            break
        elif gamestate[0]=="X" and gamestate[1]=="X" and gamestate[2] == "":
            createX3()
            break
        elif gamestate[4]=="X" and gamestate[6]=="X" and gamestate[2]=="":
            createX3()
            break
        elif gamestate[5]=="X" and gamestate[8]=="X" and gamestate[2]=="":
            createX3()
            break
        
#squares 123 AI wins game
        
        elif gamestate[0]=="X" and gamestate[6]=="X" and gamestate[3]=="":
            createX4()
            break
        elif gamestate[4]=="X" and gamestate[5]=="X" and gamestate[3]=="":
            createX4()
            break
        elif gamestate[0]=="X" and gamestate[8]=="X" and gamestate[4]=="":
            createX5()
            break
        elif gamestate[3]=="X" and gamestate[5]=="X" and gamestate[4]=="":
            createX5()
            break
        elif gamestate[6]=="X" and gamestate[2]=="X" and gamestate[4]=="":
            createX5()
            break
        elif gamestate[7]=="X" and gamestate[1]=="X" and gamestate[4]=="":
            createX5()
            break
        elif gamestate[2]=="X" and gamestate[8]=="X" and gamestate[5]=="":
            createX6()
            break
        elif gamestate[3]=="X" and gamestate[4]=="X" and gamestate[5]=="":
            createX6()
            break
        
#square 456 AI wins game
        
        elif gamestate[0]=="X" and gamestate[3]=="X" and gamestate[6]=="":
            createX7()
            break
        elif gamestate[8]=="X" and gamestate[7]=="X" and gamestate[6]=="":
            createX7()
            break
        elif gamestate[4]=="X" and gamestate[2]=="X" and gamestate[6]=="":
            createX7()
            break
        elif gamestate[1]=="X" and gamestate[4]=="X" and gamestate[7]=="":
            createX8()
            break
        elif gamestate[6]=="X" and gamestate[8]=="X" and gamestate[7]=="":
            createX8()
            break
        elif gamestate[0]=="X" and gamestate[4]=="X" and gamestate[8]=="":
            createX9()
            break
        elif gamestate[0]=="2" and gamestate[4]=="5" and gamestate[8]=="":
            createX9()
            break
        elif gamestate[0]=="6" and gamestate[4]=="7" and gamestate[8]=="":
            createX9()
            break
        
#square 789 AI wins game

        elif  gamestate[6] == "O" and gamestate[3] == "O" and gamestate[0] == "":
            createX1()
            break
        elif gamestate[2]=="O" and gamestate[1]=="O" and gamestate[0] == "":
            createX1()
            break
        elif gamestate[4]=="O" and gamestate[8]=="O" and gamestate[0] == "":
            createX1()
            break
        elif gamestate[0]=="O" and gamestate[2]=="O" and gamestate[1] == "":
            createX2()
            break
        elif gamestate[4]=="O" and gamestate[7]=="O" and gamestate[1] == "":
            createX2()
            break
        elif gamestate[0]=="O" and gamestate[1]=="O" and gamestate[2] == "":
            createX3()
            break
        elif gamestate[4]=="O" and gamestate[6]=="O" and gamestate[2]=="":
            createX3()
            break
        elif gamestate[5]=="O" and gamestate[8]=="O" and gamestate[2]=="":
            createX3()
            break
        if  gamestate[6] == "O" and gamestate[3] == "O" and gamestate[0] == "":
            createX1()
            break
        elif gamestate[2]=="O" and gamestate[1]=="O" and gamestate[0] == "":
            createX1()
            break
        elif gamestate[4]=="O" and gamestate[8]=="O" and gamestate[0] == "":
            createX1()
            break
        elif gamestate[0]=="O" and gamestate[2]=="O" and gamestate[1] == "":
            createX2()
            break
        elif gamestate[4]=="O" and gamestate[7]=="O" and gamestate[1] == "":
            createX2()
            break
        elif gamestate[0]=="O" and gamestate[1]=="O" and gamestate[2] == "":
            createX3()
            break
        elif gamestate[4]=="O" and gamestate[6]=="O" and gamestate[2]=="":
            createX3()
            break
        elif gamestate[5]=="O" and gamestate[8]=="O" and gamestate[2]=="":
            createX3()
            break
        
#squares 123 AI block player from winning
        
        elif gamestate[0]=="O" and gamestate[6]=="O" and gamestate[3]=="":
            createX4()
            break
        elif gamestate[4]=="O" and gamestate[5]=="O" and gamestate[3]=="":
            createX4()
            break
        elif gamestate[0]=="O" and gamestate[8]=="O" and gamestate[4]=="":
            createX5()
            break
        elif gamestate[3]=="O" and gamestate[5]=="O" and gamestate[4]=="":
            createX5()
            break
        elif gamestate[6]=="O" and gamestate[2]=="O" and gamestate[4]=="":
            createX5()
            break
        elif gamestate[7]=="O" and gamestate[1]=="O" and gamestate[4]=="":
            createX5()
            break
        elif gamestate[2]=="O" and gamestate[8]=="O" and gamestate[5]=="":
            createX6()
            break
        elif gamestate[3]=="O" and gamestate[4]=="O" and gamestate[5]=="":
            createX6()
            break
        
#square 456 AI block player from winning
        
        elif gamestate[0]=="O" and gamestate[3]=="O" and gamestate[6]=="":
            createX7()
            break
        elif gamestate[8]=="O" and gamestate[7]=="O" and gamestate[6]=="":
            createX7()
            break
        elif gamestate[4]=="O" and gamestate[2]=="O" and gamestate[6]=="":
            createX7()
            break
        elif gamestate[1]=="O" and gamestate[4]=="O" and gamestate[7]=="":
            createX8()
            break
        elif gamestate[6]=="O" and gamestate[8]=="O" and gamestate[7]=="":
            createX8()
            break
        elif gamestate[0]=="O" and gamestate[4]=="O" and gamestate[8]=="":
            createX9()
            break
        elif gamestate[0]=="2" and gamestate[4]=="5" and gamestate[8]=="":
            createX9()
            break
        elif gamestate[0]=="6" and gamestate[4]=="7" and gamestate[8]=="":
            createX9()
            break
        
#square 678 Ai block player from winning
        
        elif  random_int == 0 and gamestate[0] == "" :
            createX1()
            break
        elif random_int == 1 and gamestate[1] == "":
            createX2()
            break
        elif random_int == 2 and gamestate[2] == "":
            createX3()
            break
        elif random_int == 3 and gamestate[3] =="":
            createX4()
            break
        elif random_int == 4 and gamestate[4]=="":
            createX5()
            break
        elif random_int == 5 and gamestate[5]=="":
            createX6()
            break
        elif random_int == 6 and gamestate[6]=="":
            createX7()
            break
        elif random_int == 7 and gamestate[7]=="":
            createX8()
            break
        elif random_int == 8 and gamestate[8]=="":
            createX9()
            break
        elif gamestate[0] != "" and gamestate[1] != "" and gamestate[2] != "" and gamestate[3] != "" and gamestate[4] != ""and gamestate[5] != ""and gamestate[6] != ""and gamestate[7] != ""and gamestate[8] != "":
            break
        #randomly draw X in 1 - 9 squares
    print(gamestate)
    #to show player why they lost in case they didn't realize that computer can win
    if gamestate[0]== "X" and gamestate[1]== "X"  and gamestate[2] == "X":
        print("Computer win, game end")
        exit()
    elif gamestate[0]== "X" and gamestate[3]== "X" and gamestate[6] == "X":
        print("Computer win,game end")
        exit()
    elif gamestate[0]== "X" and gamestate[4] == "X"and  gamestate[8] == "X":
        print("Computer win,game end")
        exit()
    elif gamestate[1] == "X" and gamestate[4]== "X"  and gamestate [7] == "X":
        print("Computer win,game end")
        exit()
    elif gamestate[2]== "X" and gamestate[5]== "X"  and gamestate[8]== "X":
        print("Computer win,game end")
        exit()
    elif gamestate[2]== "X" and gamestate [4]== "X" and  gamestate[6]== "X":
        print("Computer win,game end")
        exit()
    elif gamestate[3]== "X" and gamestate [4]== "X" and gamestate[5]== "X":
        print("Computer win,game end")
        exit()
    elif gamestate[6] == "X"and gamestate [7]== "X" and  gamestate[8]== "X":
        print("Computer win,game end")
        exit()
    #check if computer wins
            
def draw_grid(canvas):
    canvas.create_line(0,0,0,666,666,666,666,0,0,0,width=5)
    n=0
    for i in range(2):
        canvas.create_line(222+n,0,222+n,666,width=5)
        canvas.create_line(0,222+n,666,222+n,width=5)
        n+=222
# draw grid



canvas.bind('<Button-1>', O)
#acitivates funtion  to draw O when mouse clicked in one the squares and also activates Ai to create a X
draw_grid(canvas)





root.update()
root.geometry("666x666+400+400")
root.mainloop() 
