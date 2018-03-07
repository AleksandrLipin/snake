from point import Point

class VerticalLine(Point):
    def __init__( self, x, y_up, y_down, sym ):
        self.x = x
        self.y_up = y_up
        self.y_down = y_down
        self.sym = sym

        self.point_list = []
        for y in range( self.y_up, self.y_down + 1 ):
            p = Point( self.x, y, self.sym )
            self.point_list.append(p)

    def draw(self):
        for p in self.point_list:
            print p.draw()

# some comment
