#!/usr/bin/python3

class BIT2D:
    def __init__(self):
        self.m = 0       # no. of rows
        self.n = 0       # no. of columns
        self.BIT = []    # Empty BIT

    def update(self, x, y, v):
        """x: Int, Index of row
           y: Int, Index of comlun
           v: Int, Value to be added"""
        while x <= self.m:

            # Keeping original y safe in order to iterate over responsible columns
            idxY = y
            while idxY <= self.n:

                # Updating value
                self.BIT[x][idxY] += v

                # Adding LSB in y to also update responsible indexes in that row
                # and going right
                idxY += (idxY & (-idxY))

            # Adding LSB in x to update all rows responsible for that row
            # and going up
            x += (x & (-x))

    def __calculateSum(self, x, y):
        """x: Int, Index of row
           y: Int, Index of comlun
           returns sum"""
        total = 0
        while x > 0:

            # Keeping original y safe in order to iterate over responsible indexes
            idxY = y
            while idxY > 0:

                # Accumulating sum in a variable
                total += self.BIT[x][idxY]

                # Subtracting LSB from y to go left towards lower index in that row
                idxY -= (idxY & (-idxY))

            # Subtracting LSB from x to go down and accumulating sum of responsible indexes
            x -= (x & (-x))
        return total
 
    def query(self, x1, y1, x2, y2):
        """AreaSum = Sum(OD) - Sum(OB) - Sum(OC) + Sum(OA)"""
        sumOfSubMatrix = self.__calculateSum(x2,y2) - self.__calculateSum(x2, y1 - 1) - self.__calculateSum(x1 - 1, y2) + self.__calculateSum(x1 - 1,y1 - 1)
        return sumOfSubMatrix

    def constructTree(self, matrix):
        """Main method to construct BIT"""
        self.m = len(matrix)       # rows
        self.n = len(matrix[0])    # columns

        # Initializing BIT with 2d array of m+1 rows and n+1 columns
        self.BIT = [[0 for i in range(self.m+1)] for j in range(self.n+1)]
        for i in range(self.m):
            for j in range(self.n):

                # BIT always considers index from 1 because LSB of 0 is 0
                # That's why we start it at index 1
                self.update(i+1, j+1, matrix[i][j])


# Driver Code
if __name__=='__main__':
    matrix = [[1, 1, 2, 2],
              [3, 3, 4, 4],
              [5, 5, 6, 6],
              [7, 7, 8, 8]]

    ft = BIT2D()
    ft.constructTree(matrix)
    print(ft.query(2,2,3,4))