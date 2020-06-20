import unittest
from lab_python_oop.square import square
from lab_python_oop.rect import rect
from lab_python_oop.circle import circle

class test(unittest.testcase):
    def test_rect(self):
        rect = rect(3, 2, 'синий')
        self.assertequal(str(rect), 'синий прямоугольник шириной 3, высотой 2 и площадью 6.')

    def test_circle(self):
        circle = circle(5, 'зеленый')
        self.assertequal(str(circle), 'зеленый круг радиуса 5 и площадью 78.53981633974483.')

    def test_square(self):
        square = square(5, 'красный')
        self.assertequal(str(square), 'красный квадрат со стороной 5 площадью 25.')

if __name__ == '__main__':
    unittest.main()
