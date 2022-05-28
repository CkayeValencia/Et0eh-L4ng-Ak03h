from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *

loading=Tk()


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
