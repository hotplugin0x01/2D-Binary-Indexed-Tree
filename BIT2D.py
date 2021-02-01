#!/usr/bin/python3

class FenwickTree2D:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.BIT = []

    def update(self, x, y, v):
        while x <= self.m:
            idxY = y
            while idxY <= self.n:
                self.BIT[x][idxY] += v
                idxY += (idxY & (-idxY))
            x += (x & (-x))

    def __calculateSum(self, x, y):
        total = 0
        while x > 0:
            idxY = y
            while idxY > 0:
                total += self.BIT[x][idxY]
                idxY -= (idxY & (-idxY))
            x -= (x & (-x))
        return total
 
    def getSum(self, x1, y1, x2, y2):
        """AreaSum = Sum(OD) - Sum(OB) - Sum(OC) + Sum(OA)"""
        sumOfArea = self.__calculateSum(x2,y2) - self.__calculateSum(x2, y1 - 1) - self.__calculateSum(x1 - 1, y2) + self.__calculateSum(x1 - 1,y1 - 1)
        return sumOfArea

    def constructTree(self, matrix):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.BIT = [[0 for i in range(self.m+1)] for j in range(self.n+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i+1, j+1, matrix[i][j])


# Driver Code
if __name__=='__main__':
    test1 = [[1, 1, 2, 2],
            [3, 3, 4, 4],
            [5, 5, 6, 6],
            [7, 7, 8, 8]]

    test2 = [[1, 2, 3, 4],
             [5, 3, 8, 1],
             [4, 6, 7, 5],
             [2, 4, 8, 9]]

    ft = FenwickTree2D()
    ft.constructTree(test2)
    print(ft.getSum(2,2,3,4))