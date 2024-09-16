from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, height = height, width = width)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point():
    def __init__ (self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, 
                           self.point_2.x, self.point_2.y, 
                           fill = fill_color, width = 2)

window = Window(800, 600)
point1 = Point(10, 100)
point2 = Point(20, 200)
line = Line(point1, point2)
window.draw_line(line, "red")
window.wait_for_close()