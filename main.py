
from geometry import Line, Point
from cell import Cell
from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 30, 20, 20, 20, win)
    win.wait_for_close()


if __name__ == '__main__':
    main()

