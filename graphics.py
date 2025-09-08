from tkinter import  Tk, BOTH, Canvas
from geometry import Point, Line
from cell import Cell

class Window(Tk):
    def __init__(self, width, height):
        super().__init__()
        self.title("Maze Solver")
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.update_idletasks()
        self.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()


    def close(self):
        self.running = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)