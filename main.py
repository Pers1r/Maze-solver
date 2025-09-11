from geometry import Line, Point
from cell import Cell
from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(2, 2, 10, 10, 50, 50, win, 10)
    maze.solve()
    win.wait_for_close()


if __name__ == '__main__':
    main()

