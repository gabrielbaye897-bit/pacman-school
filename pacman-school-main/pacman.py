import tkinter as tk 


window = tk.Tk()
window.title("pacman game _v2")
window.geometry("1100x800")

# select keyboard type # TO-DO / in progress.... / normaly done 
keyboardtype = None 

def ask_keyborad_layout() : 
    dialog = tk.Toplevel(window)
    dialog.title("keyboard Layout")
    dialog.geometry("250x140")
    dialog.resizable(False, False)
    dialog.grab_set()

    tk.Label(dialog, text = "what's the type of your keyboard", pady = 10).pack()

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

area = tk.Canvas(window, width = 1000, height = 750 , bg = "#000000" )
area.pack(padx = 5 , pady = 0 )

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

#keyboard layout type a/q support (qwerty/azerty)
if keyboardtype == "a":
    window.bind("<z>", Move_up)
    window.bind("<Z>", Move_up)
    window.bind("<q>", Move_left)
    window.bind("<Q>", Move_left)
    window.bind("<d>", Move_right)
    window.bind("<D>", Move_right)
    window.bind("<s>", Move_down)
    window.bind("<S>", Move_down)
else:
    window.bind("<w>", Move_up)
    window.bind("<W>", Move_up)
    window.bind("<a>", Move_left)
    window.bind("<A>", Move_left)
    window.bind("<d>", Move_right)
    window.bind("<D>", Move_right)
    window.bind("<s>", Move_down)
    window.bind("<S>", Move_down)





window.mainloop()