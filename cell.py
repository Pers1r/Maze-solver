from geometry import *


class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def get_position(self):
        return Point(self.__x1, self.__y1), Point(self.__x2, self.__y2)

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        lines = []

        point1 = Point(x1, y1)
        point2 = Point(x1, y2)
        lines.append({"line": Line (point1, point2), "color": "black" if self.has_left_wall else "#d9d9d9"})


        point1 = Point(x1, y2)
        point2 = Point(x2, y2)
        lines.append({"line": Line (point1, point2), "color": "black" if self.has_bottom_wall else "#d9d9d9"})

        point1 = Point(x2, y1)
        point2 = Point(x2, y2)
        lines.append({"line": Line (point1, point2), "color": "black" if self.has_right_wall else "#d9d9d9"})

        point1 = Point(x1, y1)
        point2 = Point(x2, y1)
        lines.append({"line": Line (point1, point2), "color": "black" if self.has_top_wall else "#d9d9d9"})
        if self.__win is not None:
            for x in lines:
                self.__win.draw_line(x['line'], color=x['color'])

    def draw_move(self, to_cell, undo=False):
        color = "grey" if undo else "red"
        pos = to_cell.get_position()
        point1 = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) /2)
        point2 = Point((pos[0].x + pos[1].x) / 2, (pos[0].y + pos[1].y) /2)
        self.__win.draw_line(Line(point1, point2), color=color)



