from point import Point

class HorizontalLine(Point):
    def __init__(self,x_left,x_right,y,sym):
        # self.point_list = point_list
        self.x_left = x_left
        self.x_right = x_right
        self.y = y
        self.sym = sym

        self.point_list = []
        for x in range(self.x_left,self.x_right):
            p = Point(x,self.y,self.sym)
            self.point_list.append(p)

    def draw(self):
        for p in self.point_list:
            print p.draw()
