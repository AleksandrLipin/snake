from point import Point

class HorizontalLine(Point):
    def __init__(self,new_list):
        self.new_list = new_list
        self.new_list = []
        p1 = Point(4,4,'*')
        p2 = Point(5,4,'*')
        p3 = Point(6,4,'*')
        self.new_list.append(p1)
        self.new_list.append(p2)
        self.new_list.append(p3)

    def draw(self):
        for p in self.new_list:
            print p.draw()
