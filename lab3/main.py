from lab_python_oop.square import Square
from lab_python_oop.rect import Rect
from lab_python_oop.circle import Circle


def main():
    rect = Rect(3, 2, 'Синий')
    circle = Circle(5, 'Зеленый')
    square = Square(5, 'Красный')

    print(rect)
    print(circle)
    print(square)


if __name__ == "__main__":
    main()
