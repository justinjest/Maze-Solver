from cell import Cell
from graphics import *
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
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
                self._cells[y].append(Cell(self.win))

        for y in range(len(self._cells)):
            for x in range(len(self._cells[y])):
                self._draw_cells(y, x)

    def _draw_cells(self, i, j):
        self._break_entrance_and_exit()
        x1 = (self.cell_size_x * j) + self.x1
        y1 = (self.cell_size_y * i) + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j]._draw_cell(x1, y1, x2, y2)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[-1][-1].has_right_wall = False

    def _animate(self):
        self.win.redraw()
        time.sleep(.005)