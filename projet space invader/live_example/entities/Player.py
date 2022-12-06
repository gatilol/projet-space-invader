class Player:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def first_display(self,canvas):
        self.player_id =  canvas.create_rectangle(
                        self.x, 
                        self.y, 
                        self.x + self.h, 
                        self.y + self.w, 
                        outline="#fb0", fill="#fb0")
        return self.player_id
