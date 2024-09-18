
from graphics import *
from cell import Cell
from maze import Maze






window = Window(800, 600)
test = Cell(window)
test.has_top_wall = False
test2 = Cell(window)
test2.has_bottom_wall = False
test2.has_top_wall = False
test2.has_left_wall = False
test2.has_right_wall = False
test._draw_cell(10, 10, 20, 20)
test2._draw_cell(20, 20, 30, 30)
test.draw_move(test2, window)
window.wait_for_close()