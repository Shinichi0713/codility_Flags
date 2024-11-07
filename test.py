import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_1_sample(self):
        A=[0 for _ in range(12)]
        A[0] = 1
        A[1] = 5
        A[2] = 3
        A[3] = 4
        A[4] = 3
        A[5] = 4
        A[6] = 1
        A[7] = 2
        A[8] = 3
        A[9] = 4
        A[10] = 6
        A[11] = 2
        self.assertEqual(solution(A), 3)
    
    def test_2_sample(self):
        self.assertEqual(solution([0,1]), 0)
    
    def test_3_sample(self):
        self.assertEqual(solution([0]), 0)

    def test_4_sample(self):
        self.assertEqual(solution([1, 1, 0])  , 0)

    def test_5_sample(self):
        self.assertEqual(solution([5, 8, 7, 5])  , 1)

unittest.main(argv=['first-arg-is-ignored'], exit=False)
