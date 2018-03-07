from point import Point
from horizontal_line import HorizontalLine
from vertical_line import VerticalLine

p1 = Point(1,2,'*')
# print(p1.draw())

p2 = Point(3,4,'#')
# print(p2.draw())

line1 = HorizontalLine(1,5,4,'*')
line1.draw()

line2 = VerticalLine(10,1,15,'$')
line2.draw()
