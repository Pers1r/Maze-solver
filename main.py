from tkinter import  Tk, BOTH, Canvas
from geometry import Line, Point

class Window(Tk):
    def __init__(self, width, height):
        super().__init__()
        self.title("Maze Solver")
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            cell1 = Cell(self)
            cell2 = Cell(self)
            cell1.draw(100, 100, 200, 200)
            cell2.draw(200, 100, 300, 200)
            cell1.draw_move(cell2)
            self.redraw()

    def close(self):
        self.running = False
        self.destroy()

    def draw_line(self, line, color):
        line.draw(self.canvas, color)



class Cell:
    def __init__(self, window):
        self.window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = -1
        self.x2 = -1
        self.y1 = -1
        self.y2 = -1
        self.win = False

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
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

    def draw_move(self, to_cell, undo=False):
        color = "grey" if undo else "red"
        point1 = Point((to_cell.x1+to_cell.x2)/2,(to_cell.y1+ to_cell.y2)/2)
        point2 = Point((self.x1+self.x2)/2, (self.y1+self.y2)/2)
        self.window.draw_line(Line(point1, point2), color=color)


win = Window(800, 600)
win.mainloop()

