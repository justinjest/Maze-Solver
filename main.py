
from graphics import *
from cell import Cell
from maze import Maze






window = Window(800, 600)
test_maze = Maze(10, 10, 12, 10, 10, 10, window)
window.wait_for_close()