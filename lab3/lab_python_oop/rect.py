from lab_python_oop.geom_figure import Figure
from lab_python_oop.color import Color

class Rect(Figure):

    type = 'Прямоугольник'

    @classmethod
    def get_figure_type(cls):
        return cls.type

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.col = Color()
        self.col.color = color

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return  '{} {} шириной {}, высотой {} и площадью {}.'.format(
            self.col.color,
            Rect.get_figure_type(),
            self.width,
            self.height,
            self.square()
        )