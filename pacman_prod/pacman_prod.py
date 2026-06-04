import tkinter as tk 
from PIL import Image, ImageTk
from random import randint



window = tk.Tk()

window.title("pacman game _v3")

Window_Height = window.winfo_screenheight() 
Window_Width = window.winfo_screenwidth()
screen_resolution = str(Window_Height)+'x'+str(Window_Width)
window.geometry(screen_resolution)

keyboardtype = None 

def ask_keyborad_layout() : 

    dialog = tk.Toplevel(window)
    dialog.title("keyboard Layout")
    Dynamic_height = Window_Height /10 
    Dynamic_Width = Window_Width /10  
    Dynamic_geometry = str(Window_Height)+'x'+str(Window_Height)
    dialog.geometry(Dynamic_geometry)
    dialog.resizable(False, False)
    dialog.grab_set()

    tk.Label(dialog, text = "what's your type of keyboard", pady = 10).pack()

    def pick(type):
        global keyboardtype
        keyboardtype = type 
        dialog.destroy()
    
    btn_frame = tk.Frame(dialog)
    btn_frame.pack()
    tk.Button(btn_frame, text = "AZERTY (a)", width = 10 , command = lambda :pick("a")).pack()
    tk.Button(btn_frame, text = "QWERTY (q)", width = 10 , command = lambda :pick("q")).pack()

    window.wait_window(dialog)

ask_keyborad_layout()

area = tk.Canvas(window ,height = Window_Height, width = Window_Width , bg = "#000000" )
area.pack(padx = 5 , pady = 0 )



pac_x1 ,pac_y1 =100 ,100
sizeofpac= 100 
pac_x2 ,pac_y2 = pac_x1 + sizeofpac , pac_y1 + sizeofpac
AngleStartCircle = 30 
rateofchange=10


def Makepac():
    area.delete("pac")
    area.create_arc(
        pac_x1 ,pac_y1 ,pac_x2 ,pac_y2,
        start = AngleStartCircle, extent =300 ,
        fill = "yellow", outline = "black", tag = "pac "
    )




#this just create it for the first time 
Makepac()


#def the mov for pacman
def Move_up(event):
    global pac_x1 ,pac_y1 ,pac_x2 ,pac_y2 ,AngleStartCircle
    pac_y1 -= rateofchange
    pac_y2 -= rateofchange
    AngleStartCircle = 90
    Makepac()

    

def Move_down(event): 
    global pac_x1 ,pac_y1 ,pac_x2 ,pac_y2 ,AngleStartCircle
    pac_y1 += rateofchange
    pac_y2 += rateofchange
    AngleStartCircle = 270
    Makepac()
    

def Move_left(event):  
    global pac_x1 ,pac_x2 ,AngleStartCircle
    pac_x1 -= rateofchange
    pac_x2 -= rateofchange
    AngleStartCircle = 180
    Makepac()

def Move_right(event): 
    global pac_x1  ,pac_x2  ,AngleStartCircle
    pac_x1 += rateofchange
    pac_x2 += rateofchange
    AngleStartCircle = 30
    Makepac()


#I have modify this to be coherent with the overall code 
# -gab

blueghost_x ,blueghost_y = 400,400
posx_gb = blueghost_x 
posy_gb = blueghost_y

def Move_ghost():
    global posx_gb , posy_gb
    x = randint(1,4)

    while(posy_gb >= Window_Width):
        x = randint(1,4)
    while(posx_gb >= Window_Height):
        x = randint(1,4)
    if (x == 1):
        area.move("blueghost", -100, 0)
        posx_gb -= 10
        area.update()
        area.after(1000)
    if (x == 2):
        area.move("blueghost", 0, -100)
        posy_gb -= 10
        area.update()
    if (x == 3):
        area.move("blueghost", 0, 100)
        posy_gb += 10
        area.update()
    if (x == 4):
        area.move("blueghost", 100, 0)
        posx_gb += 10
        area.update()

#keyboard layout type a/q support (qwerty/azerty)
if keyboardtype == "a":
    window.bind("<z>", Move_up   )
    window.bind("<Z>", Move_up   )
    window.bind("<q>", Move_left )
    window.bind("<Q>", Move_left )
    window.bind("<d>", Move_right)
    window.bind("<D>", Move_right)
    window.bind("<s>", Move_down )
    window.bind("<S>", Move_down )
else:
    window.bind("<w>", Move_up   )
    window.bind("<W>", Move_up   )
    window.bind("<a>", Move_left )
    window.bind("<A>", Move_left )
    window.bind("<d>", Move_right)
    window.bind("<D>", Move_right)
    window.bind("<s>", Move_down )
    window.bind("<S>", Move_down )

window.bind("<Up>",    Move_up   )
window.bind("<Down>",  Move_down )
window.bind("<Left>",  Move_left )
window.bind("<Right>", Move_right)


#if someone want to work on this go ahead 
#nothing keeping you back


#this need to be sync with the var :
#Window_Height
#Window_Width 

#to be addaptative pls
#and thanks you  
'''
#window_height can be x_top_right_corner
#rectangle top ,1/2 left 
#area.create_rectangle((100,100), (1800,120), width=4, outline='blue', fill='black')
#area.create_rectangle((100,100),  (120,300), width=4, outline='blue', fill='black')
area.create_rectangle((Window_height,100),(1800,500), width=4, outline='blue', fill='white')

#rectangle EF,GE,FH
#area.create_rectangle((100,830), (1800,850), width=4, outline='blue', fill='black')
#area.create_rectangle((100,330),  (120,850), width=4, outline='blue', fill='black')
#area.create_rectangle((1780,530),(1800,850), width=4, outline='blue', fill='black')

 #petit rectangle:
#IP, IJ, JK, NO, PO
#area.create_rectangle((720,340), (1080,360), width=4, outline='blue', fill='black')
#area.create_rectangle((720,340),  (740,510), width=4, outline='blue', fill='black')
#area.create_rectangle((720,490),  (885,510), width=4, outline='blue', fill='black')
#area.create_rectangle((915,490), (1080,510), width=4, outline='blue', fill='black')
#area.create_rectangle((1060,340),(1080,510), width=4, outline='blue', fill='black')
 #obstacles
#QT, UX, Ya, ac
#area.create_rectangle((240,220),(440,420),   width=4, outline='blue', fill='black')
#area.create_rectangle((120,540),(320,560),   width=4, outline='blue', fill='black')
#area.create_rectangle((240,580),(260,730),   width=4, outline='blue', fill='black')#xxx
'''



Move_ghost()

window.mainloop()































