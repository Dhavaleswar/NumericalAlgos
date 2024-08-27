import numpy as np

#improve below code and add document comments


class GaussianElimination:
    """
    Gaussian Elimination is a method to solve linear systems of equations.
    The algorithm works by transforming the system's augmented matrix into a triangular matrix.
    The algorithm is divided into two steps:
    1. Forward elimination: The algorithm transforms the matrix into an upper triangular matrix.
    2. Backward substitution: The algorithm solves the system of equations by back-substituting the values of the variables.

    The algorithm is not stable for all matrices. It may fail if the matrix is singular or ill-conditioned.
    Attributes:
    M: np.ndarray
        The augmented matrix of the system of equations.
    x: np.ndarray
        The solution to the system of equations.

    :arg
    A: np.ndarray
        The coefficient matrix of the system of equations.
    b: np.ndarray
        The right-hand side of the system of equations.
    """

    def __init__(self, A: np.ndarray, b: np.ndarray):
        self.M = A.copy()
        self.x = b.copy()

    def __forward(self):
        n_rows, n_cols = self.M.shape
        for i in range(n_rows):
            if self.M[i, i] == 0:
                for k in range(i + 1, n_rows):
                    if self.M[k, i] != 0:
                        self.__swap_rows(i, k)
                        break
            pivot = self.M[i, i]
            self.M[i] /= pivot
            self.x[i] /= pivot
            for j in range(i + 1, n_rows):
                scale_f = self.M[j, i]
                self.M[j] -= scale_f * self.M[i]
                self.x[j] -= scale_f * self.x[i]

    def __backward(self):
        n_rows, n_cols = self.M.shape
        for i in range(n_rows - 1, -1, -1):
            for j in range(i):
                scale_f = self.M[j, i]
                self.M[j, i] -= scale_f * self.M[i, i]
                self.x[j] -= scale_f * self.x[i]

    def solve(self):
        self.__forward()
        self.__backward()

    def __swap_rows(self, i, j):
        self.M[[i, j]] = self.M[[j, i]]
        self.x[[i, j]] = self.x[[j, i]]

    def __swap_cols(self, i, j):
        pass