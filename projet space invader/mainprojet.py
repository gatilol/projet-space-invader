from tkinter import *
from objet.monde import Monde

mv = Tk()
mv.title('Space Invaders')
Can=Canvas(mv, width=800, height=800, bg='white')
Can.pack()

Monde=Monde(Can)


def mainLoopCallBack():

    (x_p_0,y_p_0,x_p_1,y_p_1)=canvas.coords(Monde.joueur.j_id)

    root.after(10, mainLoopCallBack)


mv.mainloop()