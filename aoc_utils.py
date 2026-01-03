
import re


class DataGrid():

    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def get (self, x, y):
        return self.data[y][x]
    
    def set (self, x, y, value):
        self.data[y][x] = value

    def getRow (self, row):
        return self.data[row]
    
    def getCol (self, col):
        column = []
        for row in self.rows: column.append(self.data[row][col])
        return column

    def dim (self):
        return self.cols, self.rows


def ints(data: str) -> list[int]:

    '''
    Return a list of integers in the input data string. 
    
    Example:
    input: Today has 24 hours of 60 minutes.
    output: [24, 60]
    '''

    return [int(i) for i in re.findall(r"\d+", data)]


def manhattan (a: list[int], b: list[int]) -> int:
    
    '''
    Return the manhattan distance between two 2D coordinates
    
    Example:
    input: (2, 7) and (4, 9)
    outut: (4-2) + (9-7) = 4
    '''
    
    assert (len(a) == 2)
    assert (len(b) == 2)
    
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


