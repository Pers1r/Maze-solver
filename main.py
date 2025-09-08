
from geometry import Line, Point
from cell import Cell
from graphics import Window


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.draw(100, 100, 200, 200)
    cell2.draw(200, 100, 300, 200)


    win.wait_for_close()


if __name__ == '__main__':
    main()

