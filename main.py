from tkinter import Tk, BOTH, Canvas
from graphics import *



class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for y in range(self.num_cols):
            self._cells.append([])
            for x in range(self.num_rows):
                self._cells[y].append(Cell)

        for y in range(len(self._cells)):
            for x in range(y):
                self._draw_cell(y, x)

    def _draw_cell(self, i, j):
        x1 = (self.cell_size_x * j) + self.x1
        y1 = (self.cell_size_y * i) + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        Cell._draw_cell(x1, y1, x2, y2, "black", window)




window = Window(800, 600)
test = Cell(100, 100, 110, 110)
test.has_top_wall = False
test2 = Cell(90, 90, 100, 100)
test2.has_bottom_wall = False
test2.has_top_wall = False
test2.has_left_wall = False
test2.has_right_wall = False
test_maze = Maze(10, 10, 10, 10, 1, 1, 00)
test._draw_cell(test._x1, test._y1, test._x2, test._y2, "black", window)
test.draw_move(test2, window)
window.wait_for_close()