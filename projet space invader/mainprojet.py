from tkinter import * 
from objet.monde import Monde

mv = Tk()
mv.title('Space Invaders')
Can=Canvas(mv, width=800, height=700, bg='white')
Can.pack()
photo = Tk.PhotoImage(file = '.bois_noir.jpg')
fond=C.create_rectangle (0, 0, 700, 700, image=photo) 


Monde=Monde(Can)


def mainLoopCallBack():

    (x_p_0,y_p_0,x_p_1,y_p_1)=canvas.coords(Monde.joueur.j_id)
    (x_e_0,y_e_0,x_e_1,y_e_1)=canvas.coords(Monde.enemi.j_id)

    root.after(10, mainLoopCallBack)


mv.mainloop()