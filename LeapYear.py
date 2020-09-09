# This python program will tell you if a year a user enters is a leap year or not
import datetime
import tkinter as tk
from random import randint

# Function to check if a number can be cast to int
def IsInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

# Function to check current year
def GetYear():
    # Get the current year from the system clock
    sysTime = datetime.datetime.now()
    currentYear = sysTime.year
    t1.delete(0, len(t1.get()))
    t1.insert(0, currentYear)
       
# Function to get a random year
def RandYear():
    year = randint(0, 10000)
    t1.delete(0, len(t1.get()))
    t1.insert(0, year)

# Function to clear fields
def ClearFields():
    t1.delete(0, len(t1.get()))
    lbl3.config(text = "")

# Function to check if input is a leap year
def IsLeap():
    year = t1.get()
    if(IsInt(year)): 
        year = int(year)
        # Check the user's year to make sure it's valid before checking if it's a leap year
        if(year >= 0):
            if(year % 4 == 0):
                if(year % 100 == 0):
                    if(year % 400 == 0):
                        lbl3.config(text = "YES", font = ("Bold", 20), fg = "green")
                    else:
                        lbl3.config(text = "NO", font = ("Bold", 20), fg = "red")
                else:
                    lbl3.config(text = "YES", font = ("Bold", 20), fg = "green")
            else:
                lbl3.config(text = "NO", font = ("Bold", 20), fg = "red")
        else:
            lbl3.config(text = "Invalid Input", font = ("Bold", 20), fg = "red")
    else:
        lbl3.config(text = "Invalid Input", font = ("Bold", 20), fg = "red")

# GUI window
window = tk.Tk()
window.title("Leap Year Calculator")
window.geometry("400x250+10+10")
window.resizable(width = False, height = False)

# Label for year
lbl1 = tk.Label(text = "Year:")
lbl1.place(x = 50, y = 75)
# Text box to enter the year
t1 = tk.Entry(bd = 3)
t1.place(x = 100, y = 75)
# Button to use current year
btn1 = tk.Button(text = "Use Current Year", command = GetYear)
btn1.place(x = 250, y = 40)
# Button for random year between 0 and 10,000
btn2 = tk.Button(text = "Random Year", command = RandYear)
btn2.place(x = 260, y = 70)
# Button to find result
btn3 = tk.Button(text = "GO!", command = IsLeap)
btn3.place(x = 285, y = 100)
# Label for result
lbl2 = tk.Label(text = "Is it a leap year?")
lbl2.place(x = 50, y = 180)
# Label for result
lbl3 = tk.Label()
lbl3.place(x = 150, y = 170)
window.bind("<Return>", lambda event = None: btn3.invoke())
# Button to reset fields
btn4 = tk.Button(text = "Reset", command = ClearFields)
btn4.place(x = 145, y = 100)

window.mainloop()