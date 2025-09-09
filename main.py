
from geometry import Line, Point
from cell import Cell
from graphics import Window


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell1.draw(100, 100, 200, 200)
    cell2.draw(200, 100, 300, 200)
    cell1.draw_move(cell2)

    win.wait_for_close()


if __name__ == '__main__':
    main()

