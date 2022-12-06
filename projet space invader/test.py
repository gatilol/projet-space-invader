from tkinter import Tk , Label,Entry, Canvas, PhotoImage, Button


# import images_PENDU


# class pendu:
#     def init(self):
#         self.mot=""
#         self.lettrefausse=[]
        
#     def getmot(self):
#         return self.mot
        
fen=Tk()
fen.title('PENDU')

lettre=Label(fen, text="choisir la lettre ; ")
zone=Entry(fen, textvariable=lettre)
can=Canvas(fen, width= 800, height=800)
photo=PhotoImage(file="bonhomme1.gif")
item=can.create_image(250, 200, image=photo)
boutonvalidlettre=Button(fen, text="valider votre lettre")


# lettre1.grid(row=1)
lettre.grid(row=3)
zone.grid(row=4)
boutonvalidlettre.grid(row=5)
can.grid(column=3, padx=10, pady=5, sticky='nesw')


fen.mainloop()