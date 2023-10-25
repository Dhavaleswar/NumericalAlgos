from Algos.GaussianElemination import GaussianElimination
from unittest import TestCase
import numpy as np


def solve(A, b):
    gaussian_ = GaussianElimination(A, b)
    gaussian_.solve()

    b1 = A @ gaussian_.x
    check = np.allclose(b, b1, rtol=1e-5)

    print(gaussian_.x)
    print(b1)
    return check


class GaussianEliminatinTests(TestCase):
    def test_sample1(self):
        A = np.array([
            [-21, 14, 9],
            [-18, 13, 9],
            [-6, 4, 3]
        ], dtype=np.float64)
        b = np.array([[110, 94, 31]], dtype=np.float64).T
        self.assertTrue(solve(A, b))

    def test_sample2(self):
        A = np.array([
            [2, 3, -1],
            [-1, 4, 2],
            [3, -1, 1]
        ], dtype=np.float64)
        b = np.array([[1, 2, 3]], dtype=np.float64).T
        self.assertTrue(solve(A, b))
