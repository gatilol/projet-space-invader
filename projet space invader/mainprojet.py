from tkinter import *
from objet.monde import Monde
from objet.joueur import joueur
from objet.projectil import projectil
from PIL import Image, ImageTk
import os
mv = Tk()
mv.title('Space Invaders')
bg=ImageTk.PhotoImage(Image.open("projet space invader\image\earth.png"))

Can=Canvas(mv, width=700, height=700, bg='white')
Can.grid(row=2,column=0)
fond=Can.create_image(350,350,image=bg)
#os.chdir(os.path.realpath(os.path.dirname(__file__)))
#photo = PhotoImage(file = 'objet/earth.png')
#fond=Can.create_rectangle (0, 0, 700, 700,fill='#000000') 
top=Canvas(mv,width=700,height=35,bg="black")
top.grid(column=0,row=0)
buttonnewg=Button(mv,text="Nouvelle partie",width=10,command=None)
buttonquit=Button(mv, text="Quitter",width=10, command=mv.destroy)
buttonquit.place(y=7,x=620)

menubar=Menu(mv)
menumenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='menu',menu=menumenu)
menumenu.add_command(label='Commencer')
menumenu.add_command(label='Quitter', command=mv.destroy)
spaceshipe=ImageTk.PhotoImage(Image.open("projet space invader\image\spaceship.png"))
ship=Can.create_image(340,650,image=spaceshipe)
aliene=ImageTk.PhotoImage(Image.open("projet space invader\image\Alien.png"))
alien=Can.create_image(25,30,image=aliene)

global score
score=0
score=Label(mv,text="score:"+str(score),fg="white",font=50,bg="black")
score.place(x=400,y=7)
global lives
lives=3
lives=Label(mv,text="Lives left:"+str(lives),fg="white",font=50,bg="black")
lives.place(x=200,y=7)

global side
side=0

global listemissile
listemissile=[]

Monde=Monde(Can)


def mainLoopCallBack():
    b=0
    a=0
    (x_p_0,y_p_0,x_p_1,y_p_1)=Can.coords(Monde.joueur.j_id)
    (x_e_0,y_e_0,x_e_1,y_e_1)=Can.coords(Monde.enemi.j_id)
    spacemove()
    if len(listemissile)!=0:
        for i in range(len(listemissile)):
            b=listemissile[i].deplacement_proj_joueur(Can)
            a=a+b
        if a!=0:    
            for v in range(a):
                listemissile.pop(0)

    print(len(listemissile))

    Can.after(10, mainLoopCallBack)

def spacemove():
    (x_e_0,y_e_0,x_e_1,y_e_1)=Can.bbox(alien)
    bas=0
    global side
    if side%2==0:
        move=2
        if x_e_1==700:
            side=side+1     
    if side%2==1:
        move=-2
        if x_e_0==0:
            side=side+1
            bas=30      
    Can.move(alien,move,bas)
    #Can.after(100,spacemove)

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

        p = projectil(Can)
        p.creation_projectil_joueur(Can , (xj + 7.5) , (yj - 30))
        listemissile.append(p)
        
 

#utiliser piles pour le stokage des points vider la piles pour restart la game
#la game se restart apres a voir verisier que score null
#pile permet de faire un recap des types d ennemi tuée
#file pour la liste d'ennemi ?
#debut une ligne entier d enemi qui attque pas 
#deuxieme ligne apparait quand premiere ligne mort celle la attaque(anisi de suite
#creer une vitesse de deplacement pour differente difficulté

def commencer():
    mv.after(5,mainLoopCallBack)

buttonstart=Button(mv,text="Commencer",width=10,command=commencer)
buttonstart.place(y=7,x=5)

mv.bind("<Key>",keyboardCallBack)
mv.config(menu=menubar)
mv.mainloop()
