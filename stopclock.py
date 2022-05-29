from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *

loading=Tk()

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
    global location
    stopwatch = Tk()
    stopwatch.title('Stopwatch')
    stopwatch.geometry('500x500')
    

    icon = PhotoImage(file=f'{location}\\icon.png')
    stopwatch.iconphoto(False, icon)
    stopwatch.config(background="#a0dfe6")
    

    photo = PhotoImage(file=f'{location}\\background.png')

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
    pic.create_text(150,30, 
                text="4k03h L4n6 703H's Stopwatch", 
                font=("Arial", 14), 
                fill="white")
    

    stopwatch.mainloop()

    # merv

    pygame.mixer.init()
    def start():
        global ms, second, minute, starts, stop, hour, textt
        ms += 1
        if ms == 100:
            ms = 0
            second += 1
        elif second == 60:
            second = 0 
            minute += 1
        elif minute == 60:
            minute = 0
            hour += 1
        if stop == 0:
                    xms = f"0{ms}" if ms < 10 else f"{ms}"
                    xsecond = f"0{second}" if second < 10 else f"{second}"
                    xminute = f"0{minute}" if minute < 10 else f"{minute}"
                    xhour = f"0{hour}" if hour < 10 else f"{hour}"
                    textt = f"{xhour}:{xminute}:{xsecond}:{xms}"
                    TkText = Label(stopwatch, text= textt, font = ("Times 20"), fg = "white", bg = "black")
                    TkText.after(10, start)
                    TkText.place(x=183, y=223)
    def stop_watch():
        global stop
        stop = 1
        start_button['state'] = NORMAL
        pygame.mixer.music.pause()

    def reset_watch():
        global ms, second, minute, stop, music, lap
        ms, second, minute, stop, start, music = 0, 0, 0, 1, 0, 0
        TkText = Label(stopwatch, text= "00:00:00:00", font = ("Times 20"), fg = "white", bg = "black")
        TkText.place(x=183, y=223)
        start_button['state'] = NORMAL
        pygame.mixer.music.stop()
        my_listbox.delete(0, END)
        lap = 0
    
    def continue_watch():
        global stop, music
        music += 1
        if music == 1:
            pygame.mixer.music.load("C:\\Users\\Win7\\Desktop\\testset\\SxF.mp3")
            pygame.mixer.music.play(loops = -1)
        elif music > 1:
            pygame.mixer.music.unpause()
        stop = 0
        start()
        start_button['state'] = DISABLED
    #lap
    my_frame = Frame(stopwatch)
    my_scrollbar = Scrollbar(my_frame, orient=VERTICAL, background = "red")
    #listbox

    my_listbox = Listbox(my_frame, width= 15, height= 5, yscrollcommand = my_scrollbar.set, background = "green", font = ("Times 15"))
    my_scrollbar.config(command= my_listbox.yview)
    my_scrollbar.pack(side = RIGHT, fill = Y)
    my_frame.place(x=160, y = 365)
    my_listbox.place(x=160, y = 365)
    my_listbox.pack()

    def insering():
        global lap
        lap += 1
        my_listbox.insert(ANCHOR, f"{lap}.  {textt}")


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

frame_b2=Button(loading,width=10,
                height=1,
                text='Exit',
                command=exit,
                border=3,
                fg=frame_bg,
                bg='white')
frame_b2.place(x=270,y=180)


######## Label

frame_l1=Label(loading,text='4k03h L4n6 703H',
                fg='white',
                bg=frame_bg)
font_l1=('Calibri (Body)',18,'bold')
frame_l1.config(font=font_l1)
frame_l1.place(x=50,y=80)

'''
l2=Label(loading,text='SCREEN',fg='white',bg=a)
lst2=('Calibri (Body)',18)
l2.config(font=lst2)
l2.place(x=155,y=82)
'''

frame_l2=Label(loading,text='STOPWATCH',fg='white',bg=frame_bg)
font_l2=('Calibri (Body)',13)
frame_l2.config(font=font_l2)
frame_l2.place(x=50,y=110)

  

loading.mainloop()    
