from lab_python_oop.geom_figure import Figure
from lab_python_oop.color import Color
import cmath

class Circle(Figure):
    type = 'Круг'

    @classmethod
    def get_figure_type(cls):
        return cls.type

    def __init__(self,radius, color):
        self.radius = radius
        self.col = Color()
        self.col.color = color

    def square(self):
        return cmath.pi*self.radius*self.radius

    def __repr__(self):
        return '{} {} радиуса {} и площадью {}.'.format(
            self.col.color,
            Circle.get_figure_type(),
            self.radius,
            self.square()
        )