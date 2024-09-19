
from graphics import *
from cell import Cell
from maze import Maze






window = Window(800, 600)
test_maze = Maze(0, 0, 40, 30, 20, 20, window)
window.wait_for_close()