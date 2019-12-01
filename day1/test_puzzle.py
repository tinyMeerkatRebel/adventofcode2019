import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_basic_parse(self):
        masses = puzzle.parse('''12
        14
        1969
        100756'''.split())
        self.assertEqual([12, 14, 1969, 100756], masses)

    def test_basic_solve(self):
        masses = [12, 14, 1969, 100756]
        self.assertEqual(34241, puzzle.solve(masses))

    def test_pass(self):
        masses = puzzle.parse(file("puzzleInput.txt").readlines())
        answer = puzzle.solve(masses)
        self.assertEqual(3348909, answer)


if __name__ == '__main__':
    unittest.main()