# The-Tail-Bite-Snakegame
It is a small python based nokia style snake game made with the help of pygame module. It is made in order to bring in nostalgic memory of childhood period of playing nokia games.

INDEX

•	Introduction
•	Hardware and Software used
•	Data Dictionary
•	Menu Description
•	Process Logic
•	Source Code
•	Future scope of the project
•	Bibliography
 
INTRODUCTION:

Gaming is a process where we use electronic game devices that involves interaction with a user interface or input device – such as a joystick, controller, keyboard, or motion sensing device – to generate visual feedback. This feedback is shown on a video display device, such as a TV set, monitor, touchscreen, or virtual reality headset. Video games are often augmented with audio feedback delivered through speakers or headphones, and sometimes with other types of feedback, including haptic technology.

Most of the negative effects of video games arise from excessive use and addiction. Here are ten negative effects of video games:

•	Dopamine addiction
•	Reduction in Motivation
•	Alexithymia and emotional suppression
•	Repetitive stress injuries and other health risks
•	Poor mental health
•	Relationship issues
•	Social disconnection
•	Exposure to toxic gaming environments
•	Poor academic or professional performance
•	Escapism and getting stuck in life.

So there is a need for video game where the game must not cause any addiction at the same time that game must act as a stress buster. So we came with the idea of re establishing the nostalgic game from our childhood memories. That's none other than the Nokia style snake game made on latest python technology platform in a new term "the tail bite".
 
HARDWARE AND SOFTWARE USED:


Hardware:
	Processor: Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
	System type: 64-bit operating system,          x64- based processor
	Printer: HP 104A Original Black Laser.
	Keyboard: HP 4SC12PA
	Memory: RAM 8.00 GB
	Mouse: USB Optical device


Software:
	Operating System: Windows 10 Pro
	Python : Python IDLE (3.8.3 32 bit)
	MS Word : MS Word 2016 version
	Snipping tool
	Notepad
 
DATA DICTIONARY:

MODULES USED:
	turtle module
o	The turtle module provides turtle graphics primitives, in both object–oriented and procedure-oriented ways. Because it uses tkinter for the underlying graphics, it needs a version of Python installed with tkinter support
	PIL module
o	PIL module provides many ways of representing images in code, like opening them in tkinter module based buttons.
	random module
o	The random module is an inbuilt module used to generate random numbers.
	math module
o	 The math module is defined as the most famous mathematical functions, which includes log, trigonometric functions, etc.
	tkinter module
o	The tkinter is the standard GUI graphical user interface package.

MENU DESCRIPTION:

•	The Tail Bite Snake Game has three main parts.
o	Login Screen and Welcome screen
o	About and Help window
o	The main game play window.
•	Login Screen Menus
o	Username: It collects the username and stores in the text file for future processing.
o	Password: It collects the password and stores it for the future processing.
o	Login: It logs in the user and proceeds to main game screen.
o	Reset: It empties the given username and password.
o	Exit: It exits the login screen and the program terminates.
•	About and Help Window
o	About: Displays the information regarding the application in an image format
o	Help: Displays all the tips and procedures to play the game in an image format.
o	Proceed: Proceeds to the next window.
o	Logo: Displays the logo of the tail bite.
•	Main game play window menus
o	Minimize: Used to minimise the screen
o	Maximise: Used to maximise the screen and occupies the full size of monitor.
o	Close: Used to exit the program.
 
PROCESS LOGIC:

•	Login Screen
1.	We first created the Login screen with the help of tkinter, random and os module.
2.	Two name spaces called Username and Password are created which gets input from the user and stores them in a text file for future processing.
3.	 Login menu logins in the user and proceeds for the main game play.
4.	 Reset menu clears the namespaces of Username and Password. This allows the users to give the inputs once more.
5.	 Exit menu exits the login screen.
•	About and Help Window
1.	We created this window using tkinter module which have four different buttons like Help, About, Proceed, Logo whose functioning have been explained in the menu description.
2.	After clicking the proceed button, the window proceeds to the main game play window.
•	Creation of the snake
1.	 We will create snake in a specific colour by initialising variables for few colours for the snake, food, screen, etc.
2.	 We will draw the snake in form of rectangle that will grow further.
•	 Movement of the snake
1.	  To move the snake, we will use the key events present in the key down class of pygame like K_UP, K_DOWN, K_LEFT, and K_RIGHT. 
2.	 At the same time, we change the colour of the screen representing the timer.
•	Game over
1.	  Game over occurs when the snake bit its tail or if it hits the boundaries. To implement this we use the if statements along with elif.
2.	We will define the x and y directions for the boundaries.
•	Adding the food
1.	  We will make food in such a way that when the snake crosses over the food, it displays the message yummy and tasty.
2.	 By this way the food disappears after some time.
•	Control the direction of snake
1.	 We used the keyboard buttons “W” for UP and “S” for DOWN. “A” for the LEFT and “D” for RIGHT 
•	Displaying the score
1.	 We will display the score with the present score subtracted by the initial score.
2.	To do this, we will create a new function.
•	Ending the game
1.	The close menu exits the game if the player clicks on the close or X button on the right corner.
2.	The minimise button minimises the main game screen while the maximise button allows the user to play the game in full screen.
3.	It is advised to play the game in full screen for better experience.

SOURCE CODE
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
def about_help_window():
        root=tk.Tk()
        # setting the windows size 
        root.geometry("300x200")
        root.title("Help and About Window")
        root.config(bg = 'yellow')
        def about123( ):
           try :
             img2=Image.open("About.jpg")
           except IOError:
             pass
           img2.show( )
        def help123( ):
           try :
             img1=Image.open("Help.jpg")
           except IOError:
             pass
           img1.show( )
	def logo123():
	   try:
	     img3=Image.open("Logo.jpg")
	   except IOError:
	     pass
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
	logo=tk.Button(root,text='LOGO',command = logo123)
   
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

FUTURE SCOPE OF THE PROJECT:

		In future, we have decided to include multi player levels so that the players can interact with each other while playing and can also form teams.
		The main objective of this game is to bring the nostalgic childhood memories of everyone who played this nokia snake game. Such nostalgic memories act as a stress buster and escapism from the busy stressful hustling city life. 
		So we will also create an interaction platform where the players can share their nostalgic childhood memories in form of texts and audio messages. This will lead to new friendships where new opinions, thoughts and expressions can be exchanged and shared.
		In future this will act as a stress busting simple computer tool and won’t compete with the complex gaming softwares which cause addiction and indirect stress.
BIBLIOGRAPHY:

1.	Computer science with python 
	(by Sumita Arora)
2.	 Python crash course 
	(by Eric Matthews)
3.	 Learning python 
(by Mark Lutz)
