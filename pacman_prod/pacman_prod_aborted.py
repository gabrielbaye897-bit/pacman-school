import tkinter as tk 
from PIL import Image, ImageTk
from random import randint



window = tk.Tk()

window.title("pacman game _v3")

Window_Height = window.winfo_screenheight() 
Window_Width = window.winfo_screenwidth()
#screen_resolution = str(Window_Height)+'x'+str(Window_Width)
screen_resolution = str(Window_Width)+'x'+str(Window_Height)

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



#this a global var to set the global size of any case "sizegrid"

gridsize = min(Window_Width, Window_Height) // 20 








pac_x1 ,pac_y1 =100 ,100

pac_x2 ,pac_y2 = pac_x1 + gridsize , pac_y1 + gridsize
AngleStartCircle = 30 
rateofchange = gridsize


def Makepac():
    area.delete("pac")
    area.create_arc(
        pac_x1 ,pac_y1 ,pac_x2 ,pac_y2,
        start = AngleStartCircle, extent =300 ,
        fill = "yellow", outline = "black", tag = "pac"
    )




#this just create it for the first time 
Makepac()


#def the mov for pacman
def Move_up(event):
    global pac_x1 ,pac_y1 ,pac_x2 ,pac_y2 ,AngleStartCircle
    pac_y1 -= rateofchange
    pac_y2 -= rateofchange
    AngleStartCircle = 120
    Makepac()

    

def Move_down(event): 
    global pac_x1 ,pac_y1 ,pac_x2 ,pac_y2 ,AngleStartCircle
    pac_y1 += rateofchange
    pac_y2 += rateofchange
    AngleStartCircle = 300
    Makepac()
    

def Move_left(event):  
    global pac_x1 ,pac_x2 ,AngleStartCircle
    pac_x1 -= rateofchange
    pac_x2 -= rateofchange
    AngleStartCircle = 210
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
    global posx_gb, posy_gb

    if posy_gb >= Window_Height or posx_gb >= Window_Width:
        return

    x = randint(1, 4)  
    if x == 1:
        area.move("blueghost", -gridsize, 0)
        posx_gb -= gridsize
    elif x == 2:
        area.move("blueghost", 0, -gridsize)
        posy_gb -= gridsize
    elif x == 3:
        area.move("blueghost", 0, gridsize)
        posy_gb += gridsize
    elif x == 4:
        area.move("blueghost", gridsize, 0)
        posx_gb += gridsize

    window.after(500, Move_ghost)

#keyboard layout type q/a support (qwerty/azerty)
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



def verify_hitbox(x1, y1, x2, y2, ox1, oy1, ox2, oy2):
    return x1 < ox2 and x2 > ox1 and y1 < oy2 and y2 > oy1


WALL_THICKNESS = gridsize


W = Window_Width
H = Window_Height



WALLS_POS = [
    # Outer border — top, left, right
    (0.05, 0.10,  0.94, 0.12,  'pink'),    # top bar
    (0.05, 0.10,  0.07, 0.29,  'red'),     # left bar
    (0.93, 0.10,  0.94, 0.49,  'white'),   # right bar

    # Inner cage (ghost house) 
    (0.38, 0.33,  0.57, 0.35,  'blue'),   
    (0.38, 0.33,  0.39, 0.50,  'blue'),   
    (0.38, 0.48,  0.47, 0.50,  'blue'),   
    (0.48, 0.48,  0.57, 0.50,  'blue'),   
    (0.56, 0.33,  0.57, 0.50,  'blue'),   

    # Obstacles
    (0.13, 0.21,  0.23, 0.41,  'blue'),   
    (0.06, 0.53,  0.17, 0.55,  'blue'),   
    (0.13, 0.57,  0.14, 0.72,  'blue'),   
]

walls = []

for ( rx1, ry1, rx2, ry2,colorfill) in WALLS_POS:

    x1 = round(rx1 * W / gridsize) * gridsize
    y1 = round(ry1 * H / gridsize) * gridsize
    x2 = round(rx2 * W / gridsize) * gridsize
    y2 = round(ry2 * H / gridsize) * gridsize

    if x2 <= x1: x2 = x1 + gridsize
    if y2 <= y1: y2 = y1 + gridsize

    walls.append(( x1, y1, x2, y2))
    area.create_rectangle(x1 ,y1 ,x2 ,y2 , width= 2 ,outline ='blue', fill= colorfill)

def hits_wall(px1, py1, px2, py2):
    return any(verify_hitbox(px1, py1, px2, py2, *w) for w in walls)



window.mainloop()































