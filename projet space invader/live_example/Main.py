from tkinter import *
from entities.World import World 

root = Tk()
canvas_width= 500
canvas_height= 600
canvas = Canvas(root, width=canvas_width, height=canvas_height)
tx_id = canvas.create_text(100, 100, text="Hello")

w = World(canvas)
print(w.p)

canvas.pack()
def mainLoopCallBack():
    # Get coord of txt 
    (x_tx,y_tx)=canvas.coords(tx_id)
    # Get coord of player
    (x_p_0,y_p_0,x_p_1,y_p_1)=canvas.coords(w.p.player_id)
    print("Coord txt: %i,%i"%(x_tx,y_tx))
    print("Coord player: %i,%i,%i,%i"%(x_p_0,y_p_0,x_p_1,y_p_1))
    root.after(1000, mainLoopCallBack)  # reschedule event in 1 seconds

def keyboardCallBack(event):
    x = 0
    y = 0
    if event.char == "a": x = -10 
    elif event.char == "d": x = 10
    elif event.char == "w": y = -10
    elif event.char == "s": y = 10
    # move the item text with a dx and a dy
    canvas.move(tx_id, x, y)

root.after(1000, mainLoopCallBack)
root.bind("<Key>",keyboardCallBack)
root.mainloop()



