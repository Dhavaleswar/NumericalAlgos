import numpy as np


class GaussianElimination:
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