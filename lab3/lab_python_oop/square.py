from lab_python_oop.rect import Rect

class Square(Rect):
    type = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.type

    def __init__(self, length, color):
        self.length = length
        super().__init__(self.length,self.length,color)

    def __repr__(self):
        return '{} {} со стороной {} площадью {}.'.format(
            self.col.color,
            Square.get_figure_type(),
            self.length,
            self.square()
        )