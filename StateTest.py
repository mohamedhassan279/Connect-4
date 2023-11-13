import unittest
from copy import deepcopy

from State import State


class MyTestCase1(unittest.TestCase):
    def test_something(self):
        st = State()
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        correct = [deepcopy(board) for _ in range(7)]
        correct[0][0][0] = 1
        correct[1][0][1] = 1
        correct[2][0][2] = 1
        correct[3][0][3] = 1
        correct[4][0][4] = 1
        correct[5][0][5] = 1
        correct[6][0][6] = 1
        successors = st.get_successors()
        calc = [successors[i].convert_to_board() for i in range(7)]
        self.assertEqual(correct, calc)  # add assertion here


class MyTestCase2(unittest.TestCase):
    def test_something(self):
        st = State().get_successors()[0]
        board = [[1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        correct = [deepcopy(board) for _ in range(7)]
        correct[0][1][0] = 2
        correct[1][0][1] = 2
        correct[2][0][2] = 2
        correct[3][0][3] = 2
        correct[4][0][4] = 2
        correct[5][0][5] = 2
        correct[6][0][6] = 2
        successors = st.get_successors()
        calc = [successors[i].convert_to_board() for i in range(7)]
        self.assertEqual(correct, calc)  # add assertion here


class MyTestCase3(unittest.TestCase):
    def test_something(self):
        st = State().get_successors()[1]
        board = [[0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        correct = [deepcopy(board) for _ in range(7)]
        correct[0][0][0] = 2
        correct[1][1][1] = 2
        correct[2][0][2] = 2
        correct[3][0][3] = 2
        correct[4][0][4] = 2
        correct[5][0][5] = 2
        correct[6][0][6] = 2
        successors = st.get_successors()
        calc = [successors[i].convert_to_board() for i in range(7)]
        self.assertEqual(correct, calc)  # add assertion here


class MyTestCase4(unittest.TestCase):
    def test_something(self):
        st = State().get_successors()[1].get_successors()[1].get_successors()[6]
        board = [[0, 1, 0, 0, 0, 0, 1],
                 [0, 2, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        correct = [deepcopy(board) for _ in range(7)]
        correct[0][0][0] = 2
        correct[1][2][1] = 2
        correct[2][0][2] = 2
        correct[3][0][3] = 2
        correct[4][0][4] = 2
        correct[5][0][5] = 2
        correct[6][1][6] = 2
        successors = st.get_successors()
        calc = [successors[i].convert_to_board() for i in range(7)]
        self.assertEqual(correct, calc)  # add assertion here


if __name__ == '__main__':
    unittest.main()
