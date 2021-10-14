#Michael Li
#Programming 11
#2021/10/5
#Assignment 16, A tic tac toe game program but unable to tell if the square already have a X or O.
from tkinter import *
root = Tk()
canvas = Canvas(root, height=666, width=666)
canvas.pack()
b = 0
def OX(event,):
    global b
    if b == 0:
        if event.x <= 222 and event.y <= 222:
            canvas.create_oval(22,22,200,200 ,width = 5)
            b+=1
        elif event.x <= 444 and event.x >222 and event.y <= 222:
            canvas.create_oval(242,22,422,200 ,width = 5)
            b+=1
        elif event.x <=666 and event.x > 444 and event.y <= 222:
            canvas.create_oval(464,22,644,200,width=5)
            b+=1
        elif event.x<= 222 and event.y > 222 and event.y <=444:
            canvas.create_oval(22,244,200,422,width=5)
            b+=1
        elif event.x<= 444 and event.x >222 and event.y>222 and event.y <= 444:
            canvas.create_oval(244,244,422,422,width=5)
            b+=1
        elif event.x <=666 and event.x> 444 and event.y >222 and event.y <=444:
            canvas.create_oval(466,244,644,422,width=5)
            b+=1
        elif event.x <=222 and event.y >444 and event.y <=666:
            canvas.create_oval(22,466,200,644,width=5)
            b+=1
        elif event.x>222 and event.x<=444 and event.y >444 and event.y <=666:
            canvas.create_oval(244,466,422,644,width=5)
            b+=1
        elif event.x > 444 and event.x <666 and event.y>444 and event.y <=666:
            canvas.create_oval(466,466,644,644,width=5)
            b+=1
#drawing O for 1-9 squre.
    elif b == 1:
        if event.x <= 222 and event.y <= 222:
            canvas.create_line(22,22,200,200 ,width = 5)
            canvas.create_line(200,22,22,200 ,width = 5)
            b-=1
        elif event.x <= 444 and event.x >222 and event.y <= 222:
            canvas.create_line(244,22,422,200 ,width = 5)
            canvas.create_line(422,22,244,200 ,width = 5)
            b-=1
        elif event.x <=666 and event.x > 444 and event.y <= 222:
            canvas.create_line(466,22,644,200,width=5)
            canvas.create_line(644,22,466,200,width=5)
            b-=1
        elif event.x<= 222 and event.y > 222 and event.y <=444:
            canvas.create_line(22,244,200,422,width=5)
            canvas.create_line(200,244,22,422,width=5)
            b-=1
        elif event.x<= 444 and event.x >222 and event.y>222 and event.y <= 444:
            canvas.create_line(244,244,422,422,width=5)
            canvas.create_line(422,244,244,422,width=5)
            b-=1
        elif event.x <=666 and event.x> 444 and event.y >222 and event.y <=444:
            canvas.create_line(466,244,644,422,width=5)
            canvas.create_line(644,244,466,422,width=5)
            b-=1
        elif event.x <=222 and event.y >444 and event.y <=666:
            canvas.create_line(22,466,200,644,width=5)
            canvas.create_line(200,466,22,644,width=5)
            b-=1
        elif event.x>222 and event.x<=444 and event.y >444 and event.y <=666:
            canvas.create_line(244,466,422,644,width=5)
            canvas.create_line(422,466,244,644,width=5)
            b-=1
        elif event.x > 444 and event.x <666 and event.y>444 and event.y <=666:
            canvas.create_line(466,466,644,644,width=5)
            canvas.create_line(644,466,466,644,width=5)
            b-=1
#draw X in 1 - 9 squares
            
            
def draw_grid(canvas):
    canvas.create_line(0,0,0,666,666,666,666,0,0,0,width=5)
    n=0
    for i in range(2):
        canvas.create_line(222+n,0,222+n,666,width=5)
        canvas.create_line(0,222+n,666,222+n,width=5)
        n+=222
# draw grid



canvas.bind('<Button-1>', OX)
#acitivates funtion  to draw O and X when mouse clicked in one the squares.
draw_grid(canvas)





root.update()
root.geometry("666x666+400+400")
root.mainloop() 