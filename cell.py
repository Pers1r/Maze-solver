from geometry import *


class Cell:
    def __init__(self, window):
        self.window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            point1 = Point(x1, y1)
            point2 = Point(x1, y2)
            self.window.draw_line(Line(point1, point2), color="black")
        if self.has_top_wall:
            point1 = Point(x1, y2)
            point2 = Point(x2, y2)
            self.window.draw_line(Line(point1, point2), color="black")
        if self.has_right_wall:
            point1 = Point(x2, y1)
            point2 = Point(x2, y2)
            self.window.draw_line(Line(point1, point2), color="black")
        if self.has_bottom_wall:
            point1 = Point(x1, y1)
            point2 = Point(x2, y1)
            self.window.draw_line(Line(point1, point2), color="black")

