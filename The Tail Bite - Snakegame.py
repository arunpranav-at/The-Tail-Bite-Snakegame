from tkinter import*
import tkinter.messagebox                               # for messagebox
import os                                               # for stringvariable 
from tkinter import ttk                                 # for combobox
import random                                           # for reference
import time
import datetime
from PIL import Image
import turtle 
import time
import random
checking="no"

def main():
    global root
    global app
    root = Tk()
    app = Window_1(root)

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.config(bg = 'blue')
        self.Frame = Frame(self.master, bg = 'blue')
        self.Frame.pack()

        self.Username = StringVar()                             # x = StringVar()  Holds a string; default value is " "
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = 'WELCOME TO TAIL BITE GAME \n Login Menu', font = ('algerian',55,'bold'), bg = 'yellow', fg = 'black')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)
        
        self.Login_Frame_1 = LabelFrame(self.Frame, width = 1350, height = 600, relief = 'ridge', bg = 'red', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_1.grid(row = 1, column =0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width = 1000, height = 600, relief = 'ridge',bg = 'red', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_2.grid(row = 2, column = 0)

        #===========LABEL and ENTRIES========
        self.Label_Username = Label(self.Login_Frame_1, text = 'Username', font = ('arial',20,'bold'), bg = 'yellow',bd = 20)
        self.Label_Username.grid(row = 0, column = 0)
        self.text_Username = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), textvariable = self.Username)
        self.text_Username.grid(row = 0, column = 1, padx = 50)                       
        
        self.Label_Password = Label(self.Login_Frame_1, text = 'Password', font = ('arial',20,'bold'), bg = 'yellow', bd = 20)
        self.Label_Password.grid(row = 1, column = 0)
        self.text_Password = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), show = '*', textvariable = self.Password)
        self.text_Password.grid(row = 1, column = 1) 
       
        #=================BUTTONS=============
        self.btnLogin = Button(self.Login_Frame_2, text = 'Login', width = 10, font = ('calibri',15,'bold'), command = self.Login)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2, text = 'Reset', width = 10, font = ('calibri',15,'bold'), command = self.Reset)
        self.btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2, text = 'Exit', width = 10, font = ('calibri',15,'bold'), command = self.Exit)
        self.btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)

        #=================Code for Login Button===
    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())
        
        if (u != str("") and p != str("")):
            U=u
            P=p
            file1234=open("LOGIN_DETAILS.txt","a+")
            file1234.write("\n LOGIN DETAILS SAVING")
            file1234.write("\n USERNAME: ")
            file1234.write(U)
            file1234.write("\n PASSWORD: ")
            file1234.write(P)       
            file1234.close()
            file12=open("LOGIN_DETAILS.txt","a+")
            file12.read()
            file12.close()
            about_help_window()
            self.master.destroy()
        else:
            tkinter.messagebox.askyesno("Login","Error : Wrong Password")
            self.Username.set("")
            self.Password.set("")
            #self.text_Username.focus()
       
        #==========Code for Reset Button=====
    def Reset(self):
         self.Username.set("")
         self.Password.set("")
         self.text_Username.focus()

        #==========Code for Exit Button=======
    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return     

    '''def new_window(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_2(self.new_Window)'''

class Window_2:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Main Menu")
        self.master.geometry('1350x750')
        self.master.config(bg = 'red')
        self.Frame = Frame(self.master, bg = 'yellow')
        self.Frame.pack()

    

if __name__ == '__main__':                                    
    main()
    checking="yes"
#=============about and help===========
from tkinter import *
from tkinter import filedialog
import csv
import mysql.connector
from tkinter import messagebox as mb
import json
import tkinter as tk
from PIL import Image
img2=Image.open("About.jpg")
img1=Image.open("Help.jpg")
img3=Image.open("Logo.jpg")
def about_help_window():
        root=tk.Tk()
        # setting the windows size 
        root.geometry("300x200")
        root.title("Help and About Window")
        root.config(bg = 'yellow')
        def about123():
            img2.show()
        def help123():
            img1.show()
        def logo123():
            img3.show()
        def proceed123():
            root.destroy()
        
        # creating a label for  
        # name using widget Label 
        name_label = tk.Label(root, text = 'ABOUT AND HELP WINDOW', font=('calibre',10, 'bold')) 
   
        # creating a button using the widget  
        sub_btn1=tk.Button(root,text = 'ABOUT', command = about123) 
        
        # creating a button using the widget  
        sub_btn=tk.Button(root,text = 'HELP', command = help123)

        proceed_btn=tk.Button(root,text = 'PROCEED', command = proceed123)
        logo=tk.Button(root,text = 'LOGO',command = logo123)
        # placing the label and entry in 
        # the required position using grid 
        # method 
        name_label.grid(row=5,column=10) 
        sub_btn1.grid(row=8,column=5) 
        sub_btn.grid(row=8,column=15)
        proceed_btn.grid(row=20,column=10)
        logo.grid(row=8,column=10)
#==============snake game window=====
if checking=="yes":
    delay = 0.1 
    score = 0 
    high_score = 0
    wn = turtle.Screen() 
    wn.title("THE TAIL BITE - SNAKE GAME") 
    wn.bgcolor("black")
    wn.setup(width=1350, height=750) 
    wn.tracer(0)
                
    #========= head of the snake ===

    head = turtle.Turtle() 
    head.shape("circle") 
    head.color("white") 
    head.penup() 
    head.goto(0, 0) 
    head.direction = "Stop" 

    #===== food in the game ====

    food = turtle.Turtle() 
    colors = random.choice(['red', 'green', 'yellow']) 
    shapes = random.choice(['square', 'triangle']) 
    food.speed(0) 
    food.shape(shapes) 
    food.color(colors) 
    food.penup() 
    food.goto(0, 100) 
    pen = turtle.Turtle() 
    pen.speed(0) 
    pen.shape("circle") 
    pen.color("white") 
    pen.penup() 
    pen.hideturtle() 
    pen.goto(0, 250)
    pen.write(" PRESS W - UP, S - DOWN, A - LEFT, D - RIGHT \n WHITE CIRCLE IS THE SNAKE , Score: 0 High Score: 0", align="center",font=("canara",15,"bold"))

    #======= assigning key directions =====

    def goup(): 
        if head.direction != "down": 
            head.direction = "up" 
    def godown(): 
        if head.direction != "up": 
            head.direction = "down" 
    def goleft(): 
        if head.direction != "right": 
            head.direction = "left" 
    def goright(): 
        if head.direction != "left": 
            head.direction = "right" 
    def move(): 
        if head.direction == "up": 
            y = head.ycor() 
            head.sety(y+20) 
        if head.direction == "down": 
            y = head.ycor() 
            head.sety(y-20) 
        if head.direction == "left": 
            x = head.xcor() 
            head.setx(x-20) 
        if head.direction == "right": 
            x = head.xcor() 
            head.setx(x+20) 
    wn.listen() 
    wn.onkeypress(goup, "w") 
    wn.onkeypress(godown, "s") 
    wn.onkeypress(goleft, "a") 
    wn.onkeypress(goright, "d") 
    segments = [] 

    # ======== Main Gameplay ===
    while True:
        wn.update() 
        if head.xcor() > 675 or head.xcor() < -675 or head.ycor() > 375 or head.ycor() < -375: 
            time.sleep(1) 
            head.goto(0, 0) 
            head.direction = "Stop" 
            colors = random.choice(['red', 'blue', 'green']) 
            shapes = random.choice(['square', 'circle']) 
            for segment in segments: 
                segment.goto(1000, 1000) 
            segments.clear() 
            score = 0 
            delay = 0.1 
            pen.clear() 
            pen.write("Score : {} High Score : {} ".format( 
                score, high_score), align="center", font=("candara", 24, "bold")) 
        if head.distance(food) < 20: 
            x = random.randint(-270, 270) 
            y = random.randint(-270, 270) 
            food.goto(x, y) 
            # Adding segment 
            new_segment = turtle.Turtle() 
            new_segment.speed(0) 
            new_segment.shape("square") 
            new_segment.color("orange")  # tail colour 
            new_segment.penup() 
            segments.append(new_segment) 
            delay -= 0.001 
            score += 10 
            if score >high_score: 
                high_score = score    
            pen.clear() 
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold")) 

        # ====== Checking for head collisions with body segments ======

        for index in range(len(segments)-1, 0, -1): 
            x = segments[index-1].xcor() 
            y = segments[index-1].ycor() 
            segments[index].goto(x, y) 
        if len(segments) > 0: 
            x = head.xcor() 
            y = head.ycor() 
            segments[0].goto(x, y) 
        move() 
        for segment in segments: 
            if segment.distance(head) < 20: 
                time.sleep(1) 
                head.goto(0, 0) 
                head.direction = "stop" 
                colors = random.choice(['red', 'blue', 'green']) 
                shapes = random.choice(['square', 'circle']) 
                for segment in segments: 
                    segment.goto(1000, 1000) 
                segment.clear() 
                score = 0 
                delay = 0.1 
                pen.clear() 
                pen.write("Score : {} High Score : {} ".format( 
                    score, high_score), align="center", font=("candara", 24, "bold")) 
        time.sleep(delay)    
    wn.mainloop()

#========the end ======== 
