class shape(metaclass,ABCMeta):
    def __init__(self):
        print("I am in init")
    def draw_shape(self):
        pass
    def set_color(self):
        pass
class Circle(shape):
    def draw_shape(self):
        print("Draw circle")