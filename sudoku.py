from square import square
from sudokuGenerator import sudokuGenerator
import os

class sudoku:
    def __init__(self):
        self.tries = 3
        self.win = False
        self.SudokuMap = False

    def mapFromFile(self, fileStr):
        SudokuMap = []
        count = 0
        try:
            mapFile = open(fileStr,"r")
            for line in mapFile:
                SudokuLine = []
                for number in line[:-1]:
                    count += 1
                    n = int(number)
                    if n != 0:
                        SudokuLine.append(square(False,n))
                    else:
                        SudokuLine.append(square(True,n))
                SudokuMap.append(SudokuLine)
            if count == 81:
                self.SudokuMap = SudokuMap
                return True
            else:
                return False
        except:
            raise "not file found or not valid"

    def addNumber(self, number, posX , posY):
        setted = False
        if number<1 or number >9:
            print("Error el numero no es valid. Torna a probar")
        elif posX<1 or posX>9:
            print("Error la columna no es valida. Torna a probar")
        elif posY<1 or posY>9:
            print("Error la fila no es valida. Torna a probar")
        elif not self.SudokuMap[posY-1][posX-1].getType():
            print("Error aquesta casella no es pot canviar Torna a probar")
        else:
            if self.checkNum(number, posX, posY):
                self.SudokuMap[posY-1][posX-1].setNum(number)
                setted = True
            else:
                self.tries -= 1
        return setted

    def checkNum(self, number, posX , posY):
        check = True
        posX = posX - 1
        posY = posY - 1
        #comprovacio columna
        for i in range(9):
            if self.SudokuMap[i][posX].getNum() == number:
                check = False
        #comprovacio fila
        for i in range(9):
            if self.SudokuMap[posY][i].getNum() == number:
                check = False
        #comprovacio quadrant
        quadrantX = (posX // 3) * 3
        quadrantY = (posY // 3) * 3
        for i in range(quadrantX, quadrantX + 3):
            for j in range(quadrantY, quadrantY + 3):
                if self.SudokuMap[j][i].getNum() == number:
                    check = False
        return check

    def checkWin(self):
        win =True
        for i in range(9):
            for j in range(9):
                if self.SudokuMap[i][j].getNum() == 0:
                    win = False
        return win


    def printMap(self):
        print(" ")
        print("Number of lifes: ", self.tries)
        print(" ")
        for i in range(10):
            if i == 0:
                print("    1 2 3 4 5 6 7 8 9")
            else:
                print(" " * 4 + "-" * 18)
                self.printLine(i-1)
        print(" " * 4 + "-" * 18)
        print(" ")

    def printLine(self, line):
        aux = []
        for j in range(10):
            if j == 0:
                aux.append(str(line+1))
            else:
                num = self.SudokuMap[line][j-1].getNum()
                if num == 0:
                    aux.append(" ")
                else:
                    aux.append(str(num))
        auxStr = '|'.join(aux[1:])
        auxStr = aux[0] + '  |' + auxStr + '|'
        print(auxStr)

    def selectMode(self, option):
        
        if option == 1:
            self.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/saved.txt")
            return 1
        elif option == 2:
            return 2
        else:
            print("Aquesta opcio no es valida")
            return False

    def selectDificulty(self, option):
        if option == 1:
            sudokuGen = sudokuGenerator(1)
            self.SudokuMap = sudokuGen.generateMatrix()
            return True
        elif option == 2:
            sudokuGen = sudokuGenerator(2)
            self.SudokuMap = sudokuGen.generateMatrix()
            return True
        elif option == 3:
            sudokuGen = sudokuGenerator(3)
            self.SudokuMap = sudokuGen.generateMatrix()
            return True
        else:
            print("Aquesta opcio no es valida")
            return False
            