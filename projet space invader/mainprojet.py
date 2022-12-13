from tkinter import *
from objet.monde import Monde
from objet.joueur import joueur

import os
mv = Tk()
mv.title('Space Invaders')
Can=Canvas(mv, width=800, height=700, bg='white')
Can.pack()
os.chdir(os.path.realpath(os.path.dirname(__file__)))
photo = PhotoImage(file = 'objet/earth.png')
fond=Can.create_rectangle (0, 0, 700, 700,fill='#000000') 

Monde=Monde(Can)


def mainLoopCallBack():

    (x_p_0,y_p_0,x_p_1,y_p_1)=Can.coords(Monde.joueur.j_id)


    Can.after(10, mainLoopCallBack)


def deplag(event):
    """mvt du joueur a gauche """
    
    x = 0
    y = 0
    (x_p_0,y_p_0,x_p_1,y_p_1)=Can.coords(Monde.joueur.j_id)
    if x_p_0 > 0 :
        x = -10
    Can.move(Monde.joueur.j_id,x,y) 
    
    
def deplad(event):
    x = 0
    y = 0
    (x_p_0,y_p_0,x_p_1,y_p_1)=Can.coords(Monde.joueur.j_id)
    if x_p_1 < 700 :
        x = 10
    Can.move(Monde.joueur.j_id,x,y)   

 






mv.after(10,mainLoopCallBack)
mv.bind("<Left>",deplag)
mv.bind("<Right>",deplad)
mv.mainloop()