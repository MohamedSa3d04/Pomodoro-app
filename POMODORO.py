import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox

#Needed bolean variables
First = True #Indicate First period
Again = False
Stop = False
def Start_Stop():
    global work_timer, break_timer, Again, Stop, First, timer_label, timeWID, peroids_number, CurPeroid
    if startbtn.cget('text') == 'Start':
        if First :
         timeWID = tk.Toplevel(root) #A seperate widger for time consuming.
         timeWID.geometry('200x30')
         timeWID.attributes('-topmost', not root.attributes('-topmost'))

         # Remove window manager decorations
         timeWID.overrideredirect(True)

         # Create a label for the timer
         timer_label = tk.Label(timeWID, font=("Helvetica", 16),bg='black',fg='white',width='20')
         timer_label.pack()

         # Create a label for Current Peroid
         peroids_number = int(perENT.get())
         CurPeroid = tk.Label(timeWID, text=peroids_number, font=("Helvetica", 13),bg='black',fg='white',width='2')
         CurPeroid.place(x=180,y=5)

         # Get needed global values
         work_timer = int(workENT.get()) * 60
         break_timer = int(breakENT.get()) * 60
         
         
        
        Again, Stop,First = False, False, False
        workENT.config(state='readonly')
        breakENT.config(state='readonly')
        startbtn.config(text="Stop", bg="red")
        update_timer()
    else:
        Stop = True
        startbtn.config(text="Start", bg="green")


def CloseFunc():
    global Again, First
    timeWID.destroy()
    startbtn.config(text="Start", bg="green")
    workENT.config(state='normal')
    breakENT.config(state='normal')
    Again, First = True, True

def update_timer():
    global work_timer, break_timer, Again, Stop, peroids_number
    if Again :
        tempWorkTime, tempBreakTime = workENT.get(), breakENT.get()
        workENT.delete(0,100)
        breakENT.delete(0, 100)
        workENT.insert(0, tempWorkTime)
        breakENT.insert(0, tempBreakTime)
        return
    elif Stop:
        timer_label.config(fg='red')
        return
        
    elif work_timer > 0:
        work_timer -= 1 
        minutes, seconds = divmod(work_timer, 60)
        timer_label.config(text=f"Work: {minutes}:{seconds}", fg='white')
        
    else:
        # Switch to break
        if break_timer > 0:
            break_timer -= 1
            minutes, seconds = divmod(break_timer, 60)
            timer_label.config(text=f"Break: {minutes:02d}:{seconds:02d}",fg='green')
        elif peroids_number > 1 :
            # Continue the reminder peroids
            peroids_number -= 1
            CurPeroid.config(text=str(peroids_number))
            work_timer = int(workENT.get()) * 60
            break_timer = int(breakENT.get()) * 60
        else:
            # Reset the timers
            work_timer = 25 * 60
            break_timer = 5 * 60
            messagebox.showinfo("Pomodoro", "Time's up! Take a break.")
            CloseFunc() 

    # Update every second
    root.after(1000, update_timer)

root = tk.Tk()
root.title("Pomodoro Timer")
root.config(background='black')
root.geometry('300x120+600+300')


# Initialize the timer (25 minutes for work)
work_timer = 25 
break_timer = 5 
peroids_number = 1

# Creat texts box for work and break time:
worklbl = Label(root, font=('Arial',12,'bold'), fg='white', text="WorkTime:", bg='black')
worklbl.pack()
workENT = Entry(root, justify='center', width='8',fg='black')
workENT.insert(0, str(work_timer))
workENT.pack()

breaklbl = Label(root, font=('Arial',12,'bold'), fg='white', text="BreakTime:", bg='black')
breaklbl.pack()
breakENT= Entry(root, justify='center', width='8')
breakENT.insert(0, str(break_timer))
breakENT.pack()

# Number of peroids 
perlbl = Label(root, font=('Arial',7,'bold'), fg='white', text="Periods Number:", bg='black')
perlbl.pack()
perENT = Entry(root, justify='center', width='4',fg='black')
perENT.insert(0, "1")
perENT.pack()

# Creat needed buttons
startbtn = Button(root, text='Start', font=('Arial',12,'bold'), fg='white', bg='Green',command=Start_Stop)
startbtn.place(x=5,y=12)

closebtn = Button(root, text='Close', font=('Arial',12,'bold'), fg='black', bg='yellow',width=4, command = CloseFunc)
closebtn.place(x=5,y=46)


root.mainloop()
