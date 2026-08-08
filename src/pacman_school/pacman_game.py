import tkinter as tk
from random import randint

# from PIL import Image, ImageTk  

window = tk.Tk()
window.title("pacman game _v4")

Window_Height = window.winfo_screenheight()
Window_Width  = window.winfo_screenwidth()
window.geometry(f"{Window_Width}x{Window_Height}")



keyboardtype = None

def ask_keyboard_layout():
    dialog = tk.Toplevel(window)
    dialog.title("Keyboard Layout")
    sz = min(Window_Width, Window_Height) // 5
    dialog.geometry(f"{sz}x{sz}")
    dialog.resizable(False, False)
    dialog.grab_set()

    tk.Label(dialog, text="What's your keyboard layout?", pady=10).pack()

    def pick(layout):
        global keyboardtype
        keyboardtype = layout
        dialog.destroy()

    f = tk.Frame(dialog)
    f.pack()
    tk.Button(f, text="AZERTY (a)", width=12, command=lambda: pick("a")).pack(pady=4)
    tk.Button(f, text="QWERTY (q)", width=12, command=lambda: pick("q")).pack(pady=4)

    window.wait_window(dialog)

ask_keyboard_layout()


GRID_COLS = 28
GRID_ROWS = 20


gridsize = min(Window_Width // GRID_COLS, Window_Height // GRID_ROWS)

MAP_W = GRID_COLS * gridsize
MAP_H = GRID_ROWS * gridsize

area = tk.Canvas(window, width=MAP_W, height=MAP_H, bg="#000000")
area.pack(padx=5, pady=5)



WALLS_GRID = [
    # Outer border
    ( 1,  2, 27,  3, '#1a6ff5'),   # top
    ( 1,  2,  2, 18, '#1a6ff5'),   # left
    (26,  2, 27, 18, '#1a6ff5'),   # right
    ( 1, 17, 27, 18, '#1a6ff5'),   # bottom

    # Ghost cage (opening at top between col 13-15)
    (11,  8, 13,  9, '#1a6ff5'),   # top-left
    (15,  8, 17,  9, '#1a6ff5'),   # top-right
    (11,  8, 12, 12, '#1a6ff5'),   # left side
    (16,  8, 17, 12, '#1a6ff5'),   # right side
    (11, 11, 17, 12, '#1a6ff5'),   # bottom

    # Obstacles — top half
    ( 4,  4,  7,  8, '#1a6ff5'),   # top-left block
    (21,  4, 24,  8, '#1a6ff5'),   # top-right block
    (10,  4, 18,  6, '#1a6ff5'),   # top-center bar

    # Obstacles — bottom half
    ( 4, 12,  7, 16, '#1a6ff5'),   # bot-left block
    (21, 12, 24, 16, '#1a6ff5'),   # bot-right block
    (10, 14, 18, 16, '#1a6ff5'),   # bot-center bar
]

walls = []  

for (c1, r1, c2, r2, color) in WALLS_GRID:
    x1, y1 = c1 * gridsize, r1 * gridsize
    x2, y2 = c2 * gridsize, r2 * gridsize
    walls.append((x1, y1, x2, y2))
    area.create_rectangle(x1, y1, x2, y2, width=2, outline='#5599ff', fill=color)


def verify_hitbox(x1, y1, x2, y2, ox1, oy1, ox2, oy2):
    return x1 < ox2 and x2 > ox1 and y1 < oy2 and y2 > oy1

def hits_wall(col, row):
    x1 = col * gridsize
    y1 = row * gridsize
    x2 = x1 + gridsize
    y2 = y1 + gridsize
    return any(verify_hitbox(x1, y1, x2, y2, *w) for w in walls)

def in_bounds(col, row):
    return 0 <= col < GRID_COLS and 0 <= row < GRID_ROWS

def can_move(col, row):
    return in_bounds(col, row) and not hits_wall(col, row)


pac_col, pac_row   = 3, 3   # start: top-left open area
AngleStartCircle   = 30

def Makepac():
    area.delete("pac")
    x1 = pac_col * gridsize
    y1 = pac_row * gridsize
    area.create_arc(x1, y1, x1 + gridsize, y1 + gridsize,
     start=AngleStartCircle, extent=300,
     fill="yellow", outline="black", tag="pac"
    )

Makepac()

def Move_up(event):
    global pac_row, AngleStartCircle
    if can_move(pac_col, pac_row - 1):
        pac_row -= 1
        AngleStartCircle = 120
        Makepac()

def Move_down(event):
    global pac_row, AngleStartCircle
    if can_move(pac_col, pac_row + 1):
        pac_row += 1
        AngleStartCircle = 300
        Makepac()

def Move_left(event):
    global pac_col, AngleStartCircle
    if can_move(pac_col - 1, pac_row):
        pac_col -= 1
        AngleStartCircle = 210
        Makepac()

def Move_right(event):
    global pac_col, AngleStartCircle
    if can_move(pac_col + 1, pac_row):
        pac_col += 1
        AngleStartCircle = 30
        Makepac()

# col and row where ghosts spawn

ghosts = {
    "blue" :  {"col": 14, "row": 10,  "color":"cyan",    "tag": "blueghost"  },
    "red":    {"col": 13, "row": 10,  "color": "red",    "tag": "redghost"   },
    "yellow": {"col": 15, "row": 10,  "color": "yellow", "tag": "yellowghost"},
    "pink":   {"col": 16, "row": 10,  "color": "pink",   "tag": "pinkghost"  },
}

for g in ghosts.values():

    area.create_oval(
        g["col"] * gridsize,
        g["row"] * gridsize,
        g["col"] * gridsize + gridsize,
        g["row"] * gridsize + gridsize,
        fill=g["color"], outline="white", tag=g["tag"]
)

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def Move_ghost(ghost_name):

    g = ghosts[ghost_name]
    dc, dr = DIRECTIONS[randint(0, 3)]
    nc, nr = g["col"] + dc, g["row"] + dr


    if can_move(nc, nr):
        area.move(g["tag"], dc * gridsize, dr * gridsize)
        g["col"] = nc
        g["row"] = nr

    window.after(20, Move_ghost, ghost_name)

for name in ghosts :
    window.after(20, Move_ghost, name)


if keyboardtype == "a":
    window.bind("<z>", Move_up);    window.bind("<Z>", Move_up)
    window.bind("<q>", Move_left);  window.bind("<Q>", Move_left)
    window.bind("<d>", Move_right); window.bind("<D>", Move_right)
    window.bind("<s>", Move_down);  window.bind("<S>", Move_down)
else:
    window.bind("<w>", Move_up);    window.bind("<W>", Move_up)
    window.bind("<a>", Move_left);  window.bind("<A>", Move_left)
    window.bind("<d>", Move_right); window.bind("<D>", Move_right)
    window.bind("<s>", Move_down);  window.bind("<S>", Move_down)

window.bind("<Up>",    Move_up)
window.bind("<Down>",  Move_down)
window.bind("<Left>",  Move_left)
window.bind("<Right>", Move_right)

window.mainloop()