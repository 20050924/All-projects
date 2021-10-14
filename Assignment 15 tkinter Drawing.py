#Michael Li
#Programming 11
#2021/9/29
#Assignment 15, a house drawn by tkinter, when mouse clicked on somewhere will create a small dot on the spot clicked.

from tkinter import *
f=0
d=0
w=0
def XY(event):
    canvas.create_oval(event.x,event.y,event.x+1,event.y+1,fill="black",width=2)
root = Tk()
canvas = Canvas(root, height=800, width=800)
canvas.pack()
canvas.bind('<Button-1>', XY )
#create a dot when mouse clicked
canvas.create_polygon(100,300,400,100,700,300,700,600,100,600,fill="navajo white3")
#whole house
canvas.create_polygon(400,400,700,400,700,450,400,450,fill="grey")
#floor second floor
canvas.create_polygon(375,400,375,300,440,300,440,400,fill="white")
canvas.create_polygon(440,400,415,390,415,310,440,300,fill="navajo white")
canvas.create_polygon(375,600,375,500,440,500,440,600,fill="navajo white")
canvas.create_oval (380,545,390,555,fill="black",width=1)
#both door on first and second floor
for window in range(2):
    canvas.create_polygon(200+w,325,250+w,325,250+w,375,200+w,375,fill="alice blue")
    canvas.create_polygon(200+w,525,250+w,525,250+w,575,200+w,575,fill="alice blue")
    canvas.create_line(200+w,350,250+w,350,width=3)
    canvas.create_line(225+w,325,225+w,375,width=3)
    canvas.create_line(200+w,550,250+w,550,width=3)
    canvas.create_line(225+w,525,225+w,575,width=3)
    w+=350
#window
for stair in range(8):
    canvas.create_polygon(200+f,575-f,250+f,575-f,250+f,600-f,200+f,600-f,fill="grey")
    f+= 25
#stair
for rail in range(17):
    canvas.create_line(377+d,400,377+d,350,width=5)
    d+=20
canvas.create_line(375,350,700,350,width=5)
#fence

root.update()
root.geometry("800x800+400+400")
root.mainloop()