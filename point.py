class Point:
    def __init__(self,x,y,sym):
        self.x = x
        self.y = y
        self.sym = sym

    def draw(self):
        return self.x,self.y,self.sym


