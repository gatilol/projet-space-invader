from tkinter import *
from objet.monde import Monde
from objet.joueur import joueur

import os
mv = Tk()
mv.title('Space Invaders')
Can=Canvas(mv, width=700, height=700, bg='white')
Can.grid(row=2,column=0)
os.chdir(os.path.realpath(os.path.dirname(__file__)))
photo = PhotoImage(file = 'objet/earth.png')
fond=Can.create_rectangle (0, 0, 700, 700,fill='#000000') 

buttonnewg=Button(mv,text="Nouvelle partie",width=10,command=None)
buttonstart=Button(mv,text="Commencer",width=10)
buttonquit=Button(mv, text="Quitter",width=10, command=mv.destroy)
score=Label(mv,text="score:")
buttonquit.grid(row=2,column=1)
buttonstart.grid(row=00)
score.grid(row=1, column=0)

Monde=Monde(Can)


def mainLoopCallBack():

    (x_p_0,y_p_0,x_p_1,y_p_1)=Can.coords(Monde.joueur.j_id)
    (x_e_0,y_e_0,x_e_1,y_e_1)=canvas.coords(Monde.enemi.j_id)
    #(x_r_0,y_r_0,x_r_1,y_r_1)=canvas.coords(Monde.projectil.j_id)

    Can.after(10, mainLoopCallBack)


def keyboardCallBack(event):
    """mvt du joueur quand fleche direct """
    
    x = 0
    y = 0
    (x_p_0,y_p_0,x_p_1,y_p_1)=Can.coords(Monde.joueur.j_id)
    if event.keysym == "Left":
        if x_p_0 > 0 :
            x = -10
            
    elif event.keysym == "Right":
        if x_p_1 < 700 :
            x = 10
    Can.move(Monde.joueur.j_id,x,y)   








mv.after(10,mainLoopCallBack)
mv.bind("<Key>",keyboardCallBack)
mv.mainloop()