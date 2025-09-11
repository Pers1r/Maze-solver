import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0 ,num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_rows
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_cols
        )

    def test_maze_reset_cells_visited(self):
        m1 = Maze(0, 0 ,10, 10, 10, 10)
        count = 0
        for i in range(10):
            for j in range(10):
                if m1._Maze__cells[i][j].visited:
                    count += 1
        self.assertEqual(
            count,
            0
        )

if __name__ == '__main__':
    unittest.main()