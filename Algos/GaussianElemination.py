import numpy as np

class GaussianElimination:
    def __init__(self, A: np.ndarray, b:np.ndarray):
        self.M = A.copy()
        self.x = b.copy()


    def solve(self):
        n_rows, n_cols = self.M.shape
        # Forward Substitution
        for i in range(n_rows):
            if (self.M[i, i] == 0):
                for k in range(i + 1, n_rows):
                    if (self.M[k, i] != 0):
                        self.__swap_rows(i, k)
                        break
            pivot = self.M[i,i]
            self.M[i] /= pivot
            self.x[i] /= pivot
            for j in range(i+1, n_rows):
                scale_f = self.M[j,i]
                self.M[j] -= scale_f*self.M[i]
                self.x[j] -= scale_f*self.x[i]

        # Backward Substitution
        for i in range(n_rows-1, -1, -1):
            for j in range(i):
                scale_f = self.M[j,i]
                self.M[j] -= scale_f*self.M[i]
                self.x[j] -= scale_f*self.x[i]
        # self.x= self.x[self.__x_indices]

    def __swap_rows(self, i, j):
        self.M[[i,j]] = self.M[[j,i]]
        self.x[[i,j]] = self.x[[j,i]]
