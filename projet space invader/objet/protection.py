class protection:
    def __init__(self,canvas):
        self.protection_coord_x_base=50
        self.protection_coord_y_base=400
        self.protection_hauteur=40
        self.protection_largeur=40
        self.bloc=[]
        self.tbloc=[]
        self.fullprotect=[]
#creation des protections
    def creation_protection(self,canvas):
        for bloc in range (2):
            self.protection_coord_y=self.protection_coord_y_base
            

            for i in range(2):
                self.protection_coord_x=self.protection_coord_x_base
                self.protection_coord_y=self.protection_coord_y+50
                for v in range(4):
                    self.protection_coord_x=self.protection_coord_x+45
                    self.pro_id=canvas.create_rectangle(self.protection_coord_x,
                                        self.protection_coord_y,
                                        self.protection_coord_x+self.protection_largeur,
                                        self.protection_coord_y+self.protection_hauteur,
                                        outline="#000000", fill="#969292")
                    self.bloc.append(self.pro_id)
                self.tbloc.append(self.bloc)
            (x_p_0,y_p_0,x_p_1,y_p_1)=canvas.coords(self.bloc[-1])
            self.protection_coord_x_base=x_p_1+100
            self.fullprotect.append(self.tbloc)
        return self.fullprotect
