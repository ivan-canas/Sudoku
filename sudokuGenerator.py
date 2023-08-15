import numpy as np
from square import square
from random import sample,randint

class sudokuGenerator:

    def __init__(self, dificulty):
        self.dificulty = dificulty
        self.base = 3
        self.side = 9


    def shuffle(self, s): 
        return sample(s,len(s)) 

    def pattern(self,r,c): 
        return (self.base*(r%self.base)+r//self.base+c)%self.side

    def generateBase(self):
        rBase = range(self.base) 
        rows  = [ g*self.base + r for g in self.shuffle(rBase) for r in self.shuffle(rBase) ] 
        cols  = [ g*self.base + c for g in self.shuffle(rBase) for c in self.shuffle(rBase) ]
        nums  = self.shuffle(range(1,self.side+1))
        board = [ [nums[self.pattern(r,c)] for c in cols] for r in rows ]
        return board

    def remove_some(self, matrix):
        if self.dificulty == 1:
            diff = randint(12,15)
        elif self.dificulty == 2:
            diff = randint(15,19)
        elif self.dificulty == 3:
            diff = randint(19,23)
        num = diff
        while(num > 0):
            row = randint(0,8)
            col = randint(0,8)
            if matrix[row][col] != 0:
                matrix[row][col] = 0
                num -= 1
        return matrix, diff

    def generateMatrix(self):
        matrix_aux, diff = self.remove_some(self.generateBase())
        matrix = []
        count = 0
        for row_aux in matrix_aux:
            row = []
            for num in row_aux:
                count += 1
                if num == 0:
                    row.append(square( True, 0))
                else:
                    row.append(square(False, num))
            matrix.append(row)
        if count == 81:
            return matrix
        else:
            return False

    