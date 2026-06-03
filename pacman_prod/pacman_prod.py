
import tkinter as tk 
from PIL import Image, ImageTk
from random import randint


window = tk.Tk()
window.title("pacman game _v2")
window.geometry("2000x1000")

# select keyboard type # TO-DO / in progress.... / normaly done 
keyboardtype = None 

def ask_keyborad_layout() : 
    dialog = tk.Toplevel(window)
    dialog.title("keyboard Layout")
    dialog.geometry("250x140")
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

area = tk.Canvas(window, width = 1900, height = 950 , bg = "#000000" )
area.pack(padx = 5 , pady = 0 )


# here i have some code that have been copy/pasted from roman version 





area.create_arc( 100, 100, 200, 200, start = 30, extent = 300 , fill = "yellow" , outline = "yellow" , tag = "pac" )
#def the Move_Entity_d()

def Move_Entity_d( a, d, x, y,) :
    print(a)
    area.move( d, x, y)
    area.update()

#def the mov for pacman
def Move_up(event): 
    Move_Entity_d("up", "pac", 0, 100)
    area.delete("pac")
    area.create_arc( 100, 100, 200, 200, start = 120, extent = 300 , fill = "yellow" , outline = "yellow" , tag = "pac" )

def Move_down(event): 
    Move_Entity_d("down", "pac", 0, -100) 
    area.delete("pac")
    area.create_arc( 100, 100, 200, 200, start = 300, extent = 300 , fill = "yellow" , outline = "yellow" , tag = "pac" )

def Move_left(event):  
    Move_Entity_d("left", "pac", 100, 0)
    area.delete("pac")
    area.create_arc( 100, 100, 200, 200, start = 210, extent = 300 , fill = "yellow" , outline = "yellow" , tag = "pac" )

def Move_right(event): 

    Move_Entity_d("right", "pac", -100, 0)
    area.delete("pac")
    area.create_arc( 100, 100, 200, 200, start = 30, extent = 300 , fill = "yellow" , outline = "yellow" , tag = "pac" )


#def mov for ghost (idk why they didn't fcking use Move_Entity_d() )
# yeah i just c/p from others_ver/romane/romane_ver.py and this keep ghost in boundaries 
 
def Move_ghost():
    global posx_gb , posy_gb
    x = randint(1,4)

    while(posy_gb >= 950):
        x = randint(1,4)
    while(posx_gb >= 1900):
        x = randint(1,4)
    if (x == 1):
        zone.move("ghostblue", -100, 0)
        posx_gb -= 100
        zone.update()
        zone.after(1000)
    if (x == 2):
        zone.move("ghostblue", 0, -100)
        posy_gb -= 100
        zone.update()
    if (x == 3):
        zone.move("ghostblue", 0, 100)
        posy_gb += 100
        zone.update()
    if (x == 4):
        zone.move("ghostblue", 100, 0)
        posx_gb += 100
        zone.update()

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

window.bind("<Up>",  Move_up)
window.bind("<Down>", Move_down)
window.bind("<Left>", Move_left)


#rectangle AB,AC,BD
area.create_rectangle((100,100), (1800,120), width=4, outline='blue', fill='black')
area.create_rectangle((100,100),  (120,300), width=4, outline='blue', fill='black')
area.create_rectangle((1780,100),(1800,500), width=4, outline='blue', fill='black')

#rectangle EF,GE,FH
area.create_rectangle((100,830), (1800,850), width=4, outline='blue', fill='black')
area.create_rectangle((100,330),  (120,850), width=4, outline='blue', fill='black')
area.create_rectangle((1780,530),(1800,850), width=4, outline='blue', fill='black')

 #petit rectangle:
#IP, IJ, JK, NO, PO
area.create_rectangle((720,340), (1080,360), width=4, outline='blue', fill='black')
area.create_rectangle((720,340),  (740,510), width=4, outline='blue', fill='black')
area.create_rectangle((720,490),  (885,510), width=4, outline='blue', fill='black')
area.create_rectangle((915,490), (1080,510), width=4, outline='blue', fill='black')
area.create_rectangle((1060,340),(1080,510), width=4, outline='blue', fill='black')
 #obstacles
#QT, UX, Ya, ac
area.create_rectangle((240,220),(440,420),   width=4, outline='blue', fill='black')
area.create_rectangle((120,540),(320,560),   width=4, outline='blue', fill='black')
area.create_rectangle((240,580),(260,730),   width=4, outline='blue', fill='black')#xxx






Move_ghost()
window.mainloop()































