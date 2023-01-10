from tkinter import *
from objet.monde import Monde
from objet.joueur import joueur
from objet.projectil import projectil

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
    (x_e_0,y_e_0,x_e_1,y_e_1)=canvas.coords(Monde.enemi.j_id)

    Can.after(10, mainLoopCallBack)


def keyboardCallBack(event):
    """mvt du joueur gauche"""
    x = 0
    y = 0
    (x_p_0,y_p_0,x_p_1,y_p_1)=Can.coords(Monde.joueur.j_id)
    if event.keysym == "Left":
        if x_p_0 > 0 :
            x = -10
    
    """mvt du joueur droite"""

    if event.keysym == "Right":  
    
        if x_p_1 < 700 :
            x = 10
    Can.move(Monde.joueur.j_id,x,y)   


    if event.keysym == "space" :
        (xj,yj,lj,hj)=Can.coords(Monde.joueur.j_id)

        print("1854132186")
        p = projectil(Can)
        p.creation_projectil_joueur(Can , (xj + 2.5) , (yj + 30))
        p.deplacement_proj_joueur(Monde.projectil.pj_id)

 






mv.after(5,mainLoopCallBack)
mv.bind("<Key>",keyboardCallBack)
mv.mainloop()