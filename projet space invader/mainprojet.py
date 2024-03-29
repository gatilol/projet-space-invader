from tkinter import *
from tkinter import messagebox
from objet.monde import Monde
from objet.joueur import joueur
from objet.enemi import enemi
from objet.projectil import projectil
from PIL import Image, ImageTk
import os

#creation fenetre Tkinter
mv = Tk()
mv.title('Space Invaders')

#load des images 
bg=ImageTk.PhotoImage(Image.open("projet space invader\image\earth.png"))
aliene=ImageTk.PhotoImage(Image.open("projet space invader\image\Alien.png"))
spaceshipe=ImageTk.PhotoImage(Image.open("projet space invader\image\spaceship.png"))

#creation de la zone de jeu et bordure pour bouton, score et pt de vie
Can=Canvas(mv, width=700, height=700, bg='white')
top=Canvas(mv,width=700,height=35,bg="black")

#creation des bouton
buttonnewg=Button(mv,text="Nouvelle partie",width=10,command=None)
buttonquit=Button(mv, text="Quitter",width=10, command=mv.destroy)


#positionnement sur la fenetre
top.grid(column=0,row=0)
buttonquit.place(y=7,x=620)
Can.grid(row=2,column=0)
fond=Can.create_image(350,350,image=bg)

#creation des du vaiseau et d'un enemi
ship=Can.create_image(340,650,image=spaceshipe)
#alien=Can.create_image(25,30,image=aliene)

#stockage et affichage du score et du nb de vie:
global score
score=0
score=Label(mv,text="score:"+str(score),fg="white",font=50,bg="black")
score.place(x=400,y=7)
global lives
lives=3
lives=Label(mv,text="Lives left:"+str(lives),fg="white",font=50,bg="black")
lives.place(x=200,y=7)



global listemissile
listemissile=[]



#fonction qui ferme le programme ou le relancer s'il le joueur pert
def lose_condition():
    answer=messagebox.askretrycancel("YOU LOSE","Voulez vous réessayer?") 
    if answer==True:
        commencer()
    else:
        mv.destroy()

Monde=Monde(Can, aliene)

def mainLoopCallBack():
    b=0
    a=0
    c=0
    d=0
    (x_p_0,y_p_0,x_p_1,y_p_1)=Can.bbox(ship)
    #(x_e_0,y_e_0,x_e_1,y_e_1)=Can.coords(Monde.enemi.e_id)
    #enemi_move()
    #enemi.enemi_move2(Can)
    Monde.enemi.movement(Can)


    if len(listemissile)!=0:
        for i in range(len(listemissile)):
            b=listemissile[i].deplacement_proj_joueur(Can)
            a=a+b
        if a!=0:    
            for v in range(a):
                listemissile.pop(0)
    
    if len(listemissile)!=0:
        for i in range(len(listemissile)):
            c=listemissile[i].veriftoucherprotectj(Can,Monde.protection.fullprotect)
            if c!=0:
                listemissile.pop(i)

    if len(listemissile)!=0:
        for i in range(len(listemissile)):
            d=listemissile[i].veriftoucherenemi(Can,Monde.enemi.liste_enemi)
            if d!=0:
                listemissile.pop(i)

    
    
               
    Can.after(100, mainLoopCallBack)


#fonction pour bouger les enemis image
global side
side=0

#fontion qui permet de fire bouger un enemi seul fonction remplacer par la fct movement(dans classe)
def enemi_move():
    bas=0
    (x_e_0,y_e_0,x_e_1,y_e_1)=Can.bbox(alien)
    global side
    if side%2==0:
        move=30
        if x_e_1>=900:
            side=side+1  
            bas=30   
    if side%2==1:
        move=-30
        if x_e_0<=-200:
            side=side+1
            bas=30
    if y_e_0==615:
        lose_condition()              
    Can.move(alien,move,bas)


#fonction pour les mouvements du joueur(vaiseau)[droite, gauche, tire]
def keyboardCallBack(event):
    """mvt du joueur gauche"""
    x = 0
    y = 0
    (x_p_0,y_p_0,x_p_1,y_p_1)=Can.bbox(ship)
    if event.keysym == "Left":
        if x_p_0 > 0 :
            x = -10
    
    """mvt du joueur droite"""

    if event.keysym == "Right":
    
        if x_p_1 < 700 :
            x = 10
    Can.move(ship,x,y)   

    
    if event.keysym == "space" :
        (xj,yj,lj,hj)=Can.bbox(ship)
        global score
        p = projectil(Can)
        p.creation_projectil_joueur(Can , (xj + 17.5) , (yj - 30))
        listemissile.append(p)

#fonction qui permet de lancer les mouvement et permettre le commencement du jeu
def commencer():

    mv.after(5,mainLoopCallBack)
#bouton commencer
buttonstart=Button(mv,text="Commencer",width=10,command=commencer)
buttonstart.place(y=7,x=5)

#code cheat remer les enemies au debut


#barre du menu
menubar=Menu(mv)
menumenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='menu',menu=menumenu)
menumenu.add_command(label='Commencer',command=commencer)
menumenu.add_command(label='Quitter', command=mv.destroy)
mv.config(menu=menubar)

mv.bind("<Key>",keyboardCallBack)

mv.mainloop()