import unittest
from random import choice, randint

from app import Figure


class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконається лише раз на початку тестів"""
        pass

    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест"""
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_lengh(self):
        self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає непривильну довжину!")

    def test_obj(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_get_angles(self):
        # Тестуємо що для трикутника повертається 3, для квадрата 4
        tri = Figure("трикутник", 1)
        sq = Figure("квадрат", 1)
        self.assertEqual(tri.get_angles, 3, "У трикутника має бути 3 кути")
        self.assertEqual(sq.get_angles, 4, "У квадрата має бути 4 кути")


if __name__ == '__main__':
    unittest.main()
