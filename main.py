
from tkinter import *
import customtkinter 
import pyautogui as pg
import time


# opening apps  

def openApp(App_name):
    pg.press('win')
    pg.sleep(1)
    pg.write(App_name)
    pg.press('enter')
    pg.sleep(1)


def allignWindow(windowPosition):
    
    pg.hotkey('win',windowPosition)
    pg.sleep(2)


def get_radio():
    if radio_var.get() == "other":
        my_label2.configure(text='other')

    elif radio_var.get() == "coding":
        my_label2.configure(text='coding')

        # coding 
        # openApp('music')
        # openApp('brave')
        # allignWindow('left')
        # openApp('vscode')
        # app.destroy()



    elif radio_var.get() == "gaming":
        my_label2.configure(text='gamimg')



    elif radio_var.get() == "editing":
        my_label2.configure(text='editing')
    

def update_action():
    time_up_label.configure(text=radio_var.get() + " is being executed")
    my_button.invoke()
    

customtkinter.set_appearance_mode('dark')


app = customtkinter.CTk()

app.title('Auto Desk')
app.geometry('700x400')


my_label = customtkinter.CTkLabel(app,text="choose your options")
my_label.pack(pady=40)

radio_var = customtkinter.StringVar(value='other')

#radio button 1 
my_rad1 = customtkinter.CTkRadioButton(app,text="Coding", value="coding",variable=radio_var)
my_rad1.pack(pady=10)

my_rad2 = customtkinter.CTkRadioButton(app,text="editing",value='editing',variable=radio_var)
my_rad2.pack(pady=10)

my_rad3 = customtkinter.CTkRadioButton(app,text="gaming",value='gaming',variable=radio_var)
my_rad3.pack(pady=10)

my_button = customtkinter.CTkButton(app,text='select',command=get_radio)
my_button.pack(pady=10)


my_label2 = customtkinter.CTkLabel(app,text='')
my_label2.pack(padx=20,pady=10)

time_up_label = customtkinter.CTkLabel(app,text='you have 10 sec to choose')
time_up_label.pack(pady=10)
time_up_label.after(5000,update_action)



app.mainloop()



