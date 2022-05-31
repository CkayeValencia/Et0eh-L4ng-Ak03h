from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import time
import os
import pygame

loading=Tk()
location = os.getcwd()
ms = 0
second = 0
minute = 0
hour = 0
stop = 0 
starts = 0
music = 0
lap = 0

window_width = 427
window_height = 250
screen_width = loading.winfo_screenwidth()
screen_height = loading.winfo_screenheight()
line_x = (screen_width/2)-(window_width/2)
line_y = (screen_height/2)-(window_height/2)
loading.geometry("%dx%d+%d+%d" %(window_width,window_height,line_x,line_y))


loading.overrideredirect(1)
loading.configure(cursor="heart")

theme = ttk.Style()
theme.theme_use('clam')
theme.configure("red.Horizontal.TProgressbar", 
                foreground='red', 
                background='#4f4f4f')

progress=Progressbar(loading,style="red.Horizontal.TProgressbar",
                    orient=HORIZONTAL,
                    length=500,
                    mode='determinate',)

def stopwatch_GUI():
    global location, ms, second, minute, hour, stop, starts, music
    stopwatch = Tk()
    stopwatch.title('Stopwatch')
    stopwatch.geometry('500x500')
    # code to pop the gui to the center of the screen
    xxxwidth_of_window = 500
    xxxheight_of_window = 500
    xxxscreen_width = stopwatch.winfo_screenwidth()
    xxxscreen_height = stopwatch.winfo_screenheight()
    xxxx_coordinate = (xxxscreen_width/2)-(xxxwidth_of_window/2)
    yyyy_coordinate = (xxxscreen_height/2)-(xxxheight_of_window/2)
    stopwatch.geometry("%dx%d+%d+%d" %(xxxwidth_of_window,xxxheight_of_window,xxxx_coordinate,yyyy_coordinate))
    
    icon = PhotoImage(file=f"{location}\\icon.png")
    stopwatch.iconphoto(False, icon)
    stopwatch.config(background="#a0dfe6", cursor="heart")

    photo = PhotoImage(file=f"{location}\\background.png")

    pic = Canvas(stopwatch,
            width=500, 
            height=500,
            bg='black', 
            relief=RAISED, 
            bd=10,)

    pic.pack(padx=0,pady=0, 
        expand=True)  

    pic.create_image(0,0, 
        image = photo, 
        anchor = "nw",)

    pic.create_text(250,275, 
                text="4k03h L4n6 703H's Stopwatch", 
                font=("Arial", 8), 
                fill="aquamarine")

    pygame.mixer.init()
    def start():
        global ms, second, minute, starts, stop, hour, timeer, buttoninsert
        if(stop==0):
            timeer = str(timee.get())
            hour,minute,second,ms = map(int,timeer.split(":")) 
            hour = int(hour)
            minute = int(minute)
            second=int(second)
            ms= int(ms)
            if(ms<99):
                ms+=1
            elif(ms==99):
                ms=0
                if(second<59):
                    second+=1
                elif(second==59):
                    second=0
                    if(minute<59):
                        minute+=1
                    elif(minute==59):
                        hour+=1
            if(hour<10):
                hour = str(0)+str(hour)
            else:
                hour= str(hour)
            if(minute<10):
                minute = str(0)+str(minute)
            else:
                minute= str(minute)
            if(second<10):
                second = str(0)+str(second)
            else:
                second = str(second)
            if(ms<10):
                ms=str(0)+str(ms)
            else:
                ms=str(ms)
            timeer=hour+":"+minute+":"+second+":"+ms
            timee.set(timeer)
            if(stop==0):
                time.sleep(0.00095)
                stopwatch.after(9, start)
                    
    def stop_watch():
        global stop
        stop = 1
        start_button = Button(stopwatch, image = start_bttn, command=continue_watch, borderwidth=5)
        start_button.place(x =157, y = 293)
        reset_button = Button(stopwatch, image = reset_bttn, command=reset_watch, borderwidth=5)
        reset_button.place(x=300, y = 293)
        pygame.mixer.music.pause()
        exxiit_button['state'] = NORMAL
 
    def reset_watch():
        global ms, second, minute, stop, music, lap
        ms, second, minute, stop, start, music = 0, 0, 0, 1, 0, 0
        timee.set('00:00:00:00')
        start_button['state'] = NORMAL
        pygame.mixer.music.stop()
        LapBox.delete(0, END)
        lap = 0
        lap_button['state'] = DISABLED
        exxiit_button['state'] = NORMAL

    def continue_watch():
        global stop, music
        music += 1
        if music == 1:
            pygame.mixer.music.load(f"{location}\\SxF.mp3")
            pygame.mixer.music.play(loops = -1)
        elif music > 1:
            pygame.mixer.music.unpause()
        stop = 0
        start()
        stop_button = Button(stopwatch, image = stop_bttn, command= stop_watch, borderwidth=5)
        stop_button.place(x=157, y = 293)
        lap_button = Button(stopwatch, image = lap_bttn, command=insering, borderwidth=5)
        lap_button.place(x=300, y = 293)
        exxiit_button['state'] = DISABLED
    
    #confirmation exit
    def confirming():
        def ifyes():
            ConfirmEXT.destroy()
            stopwatch.destroy()
        def ifno():
            exxiit_button['state'] = NORMAL
            ConfirmEXT.grab_release()
            ConfirmEXT.destroy()
        
        exxiit_button['state'] = DISABLED
        ConfirmEXT = Toplevel()
        ConfirmEXT.title('Confirmation')
        ConfirmEXT.geometry('170x50')
        ConfirmEXT.grab_set()
        xxwidth_of_window = 170
        xxheight_of_window = 50
        xxscreen_width = ConfirmEXT.winfo_screenwidth()
        xxscreen_height = ConfirmEXT.winfo_screenheight()
        xxx_coordinate = (xxscreen_width/2)-(xxwidth_of_window/2)
        yyy_coordinate = (xxscreen_height/2)-(xxheight_of_window/2)
        ConfirmEXT.geometry("%dx%d+%d+%d" %(xxwidth_of_window,xxheight_of_window,xxx_coordinate,yyy_coordinate))
        ConfirmEXT.overrideredirect(1)
        

        secondframeconfirmationlabel = tk.Label(ConfirmEXT, text = "Are you really going to leave? :(")
        secondframeconfirmationlabel.place(x = 0, y = 0)
        Yespls = tk.Button(ConfirmEXT, text = "Yes", command = ifyes, bg= "orange")
        Yespls.place(x = 53, y = 20)

        plsNo = tk.Button(ConfirmEXT, text = "No", command = ifno, bg= "orange")
        plsNo.place(x = 83, y = 20)
        ConfirmEXT.resizable(0, 0)
        ConfirmEXT.mainloop()

    timee = StringVar()
    timee.set("00:00:00:00")
    lb = Label(stopwatch,textvariable=timee,font = ("Times 40"), fg = "white", bg = "black")
    lb.place(x=118, y=197)
# lap
    LapFrame = Frame(stopwatch, bd=0, background = "green")
    Lapscrollbar = Scrollbar(LapFrame, orient=VERTICAL, troughcolor = "red", bg = 'black', width= 0)
# listbox
    LapBox = Listbox(LapFrame, width= 18, height= 4, yscrollcommand = Lapscrollbar.set, background = "#B43757", font = ("Times 18"), bd = 0, fg = "#D9DDDC")
    Lapscrollbar.config(command= LapBox.yview, troughcolor = "red", bg = 'black')
    Lapscrollbar.pack(side = RIGHT, fill = Y)
    LapFrame.place(x=142, y = 365)
    LapBox.place(x=142, y = 365)
    LapBox.pack()

    def insering():
        global lap, timeer
        lap += 1
        LapBox.insert(0, f"  {lap}.  {timeer}")

# start image
    start_pic = Image.open(f"{location}\\Start.png")
    resized = start_pic.resize((33, 33), Image.ANTIALIAS)
    start_bttn = ImageTk.PhotoImage(resized)
# stop image
    stop_pic = Image.open(f"{location}\\Stop1.png")
    resized = stop_pic.resize((33, 33), Image.ANTIALIAS)
    stop_bttn = ImageTk.PhotoImage(resized)
# reset image
    reset_pic = Image.open(f"{location}\\Reset.png")
    resized = reset_pic.resize((33, 33), Image.ANTIALIAS)
    reset_bttn = ImageTk.PhotoImage(resized)
# lap image
    lap_pic = Image.open(f"{location}\\Lap.png")
    resized = lap_pic.resize((33, 33), Image.ANTIALIAS)
    lap_bttn = ImageTk.PhotoImage(resized)
# stop Button
    stop_button = Button(stopwatch, image = stop_bttn, command= stop_watch, borderwidth=5)
    stop_button.place(x=157, y = 293)
# start Button
    start_button = Button(stopwatch, image = start_bttn, command=continue_watch, borderwidth=5)
    start_button.place(x =157, y = 293)
# Lap Button
    lap_button = Button(stopwatch, image = lap_bttn, command=insering, borderwidth=5)
    lap_button.place(x=300, y = 293)
# Reset Button
    reset_button = Button(stopwatch, image = reset_bttn, command=reset_watch, borderwidth=5)
    reset_button.place(x=300, y = 293)
# Exit Button
    exxiit_button = Button(stopwatch, text= "Exit", command=confirming, borderwidth=5, bg= "red", fg = "white")
    exxiit_button.place(x=450, y = 460)
    
    stopwatch.resizable(0, 0)

    stopwatch.mainloop()



def run():

    label_run=Label(loading,text='Loading...',fg='white',bg=frame_bg)
    Label4_font=('Calibri (Body)',10)
    label_run.config(font=Label4_font)
    label_run.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        loading.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    loading.destroy()
    stopwatch_GUI()
        
progress.place(x=-10,y=235)

# exit confirmation 1st interface
def confirming1():
        global frame_b2
        frame_b2['state'] = DISABLED
        def yesif():
            EXTconfirm.destroy()
            loading.destroy()
        def noif():
            frame_b2['state'] = NORMAL
            EXTconfirm.destroy()
            EXTconfirm.grab_release()
            
        

        EXTconfirm = Toplevel()
        EXTconfirm.title('Confirmation')
        EXTconfirm.geometry('170x50')
        EXTconfirm.grab_set()
        xwidth_of_window = 170
        xheight_of_window = 50
        xscreen_width = EXTconfirm.winfo_screenwidth()
        xscreen_height = EXTconfirm.winfo_screenheight()
        xx_coordinate = (xscreen_width/2)-(xwidth_of_window/2)
        yy_coordinate = (xscreen_height/2)-(xheight_of_window/2)
        EXTconfirm.geometry("%dx%d+%d+%d" %(xwidth_of_window,xheight_of_window,xx_coordinate,yy_coordinate))
        EXTconfirm.overrideredirect(1)
        ConfirmingTXT = tk.Label(EXTconfirm, text = "Are you really going to leave? :(")
        ConfirmingTXT.place(x = 0, y = 0)

        Yespls = tk.Button(EXTconfirm, text = "Yes", command = yesif, bg= "orange")
        Yespls.place(x = 53, y = 20)

        plsNo = tk.Button(EXTconfirm, text = "No", command = noif, bg= "orange")
        plsNo.place(x = 83, y = 20)
        EXTconfirm.resizable(0, 0)
        EXTconfirm.mainloop()

def exit():
    loading.destroy()

frame_bg='#249794'

Frame(loading,width=427,
            height=241,
            bg=frame_bg,).place(x=0,y=0)  #249794
frame_b1=Button(loading,width=10,
                height=1,
                text='Get Started',
                command=run,
                border=3,fg=frame_bg,
                bg='white')
frame_b1.place(x=70,y=180)

frame_frame_b2=Button(loading,width=10,
                height=1,
                text='Exit',
                command=confirming1,
                border=3,
                fg=frame_bg,
                bg='white')
frame_frame_b2.place(x=270,y=180)


######## Label

frame_l1=Label(loading,text='4k03h L4n6 703H',
                fg='white',
                bg=frame_bg)
font_l1=('Calibri (Body)',18,'bold')
frame_l1.config(font=font_l1)
frame_l1.place(x=50,y=80)

frame_l2=Label(loading,text='STOPWATCH',fg='white',bg=frame_bg)
font_l2=('Calibri (Body)',13)
frame_l2.config(font=font_l2)
frame_l2.place(x=50,y=110)

loading.mainloop()    
