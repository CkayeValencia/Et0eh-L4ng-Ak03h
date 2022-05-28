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
