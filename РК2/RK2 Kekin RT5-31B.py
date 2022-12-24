import unittest
import RK1


class testRK1(unittest.TestCase):
    def setUp(self):
        self.test1 = (['D:\\программы на python', 'C:\\игры'], ['Hello world.py', 'game.py'])
        self.test2 = [['D:\\программы на python', 1500], ['D:\\отчёты по лабам', 100], ['C:\\игры', 0]]
        self.test3 = [['game.py', ['D:\\программы на python', 'C:\\игры']]]

    def test1_rk(self):
        self.assertEqual(RK1.task1(RK1.oneToMany), self.test1)

    def test2_rk(self):
        self.assertEqual(RK1.task2(RK1.oneToMany), self.test2)

    def test3_rk(self):
        self.assertEqual(RK1.task3(RK1.manyToMany), self.test3)


if __name__ == '__main__':
    unittest.main()
