from tkinter import Tk, BOTH, Canvas
from graphics import *
from cell import Cell
from maze import Maze






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