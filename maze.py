from cell import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = [[ _ for _ in range(num_cols)] for _ in range(num_rows)]
        self.__create_cells()

    def __create_cells(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.__cells[row][col] = Cell(self.win)
                self.__draw_cell(row, col)

    def __draw_cell(self, row, col):
        x1 = self.x1 + self.cell_size_x * row
        x2 = self.x1 + self.cell_size_x * (row+1)
        y1 = self.y1 + self.cell_size_y * col
        y2 = self.y1 + self.cell_size_y * (col+1)
        self.__cells[row][col].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        self.win.redraw()
        time.sleep(0.05)

