import unittest
import sys
sys.path.insert(1, '/home/ivan/Desktop/TQS_pract')
from sudoku import sudoku

class TestSudokuMethods(unittest.TestCase):
    def test_select_mode(self):
        sudoku_test = sudoku()
        # valors frontera
        self.assertTrue(sudoku_test.selectMode(1))
        self.assertTrue(sudoku_test.selectMode(2))
        # valors externs frotera
        self.assertFalse(sudoku_test.selectMode(0))
        self.assertFalse(sudoku_test.selectMode(3))
        self.assertFalse(sudoku_test.selectMode(-1))

    def test_select_dificulty(self):
        sudoku_test = sudoku()
        # valors frontera
        self.assertTrue(sudoku_test.selectDificulty(1))
        self.assertTrue(sudoku_test.selectDificulty(3))
        # valor intern frontera
        self.assertTrue(sudoku_test.selectDificulty(2))
        # valors externs frotera
        self.assertFalse(sudoku_test.selectDificulty(0))
        self.assertFalse(sudoku_test.selectDificulty(4))
        self.assertFalse(sudoku_test.selectDificulty(-1))

    def test_map_from_file(self):
        sudoku_test = sudoku()
        # path real d'un fitxer amb un mapa valid
        self.assertTrue(sudoku_test.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/saved.txt"))
        # path real d'un fitxer amb un mapa no valid
        self.assertFalse(sudoku_test.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/wrong.txt"))
        # path no real
        with self.assertRaises(TypeError):
            sudoku_test.mapFromFile("pepe.txt")

    def test_add_number(self):
        # sudoku add number necesita de tenir la matriu inicialitzada
        # no s'ha implementat un mock object per fer aixo ja que la matriu esta formada per objectes square no per numeros
        # aixo fa que la implementacio d'un mock object sigui bastant complexa 
        # i s'ha cregut mes convenient cridar a la funcio mapFromFile que propociona un sudocku correcte
        sudoku_test = sudoku()
        sudoku_test.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/saved.txt")
        # pairwaise (evitem les nombroses posibilitats de fer valor frontera a num, posX i posY)
        # opcions [0,[1,9],10]
        self.assertFalse(sudoku_test.addNumber(0,0,0))
        self.assertFalse(sudoku_test.addNumber(0,1,10))
        self.assertFalse(sudoku_test.addNumber(0,10,1))
        # unica convinatoria que afegir numeros, probem per un numero 
        # que compleixi les regles del sudoku al nostre mapa i un que no
        self.assertFalse(sudoku_test.addNumber(1,1,1)) #no valid
        self.assertTrue(sudoku_test.addNumber(4,1,1)) #valid
        #
        self.assertFalse(sudoku_test.addNumber(1,10,0))
        self.assertFalse(sudoku_test.addNumber(1,0,10))
        self.assertFalse(sudoku_test.addNumber(10,10,10))
        self.assertFalse(sudoku_test.addNumber(10,0,1))
        self.assertFalse(sudoku_test.addNumber(10,1,0))
        
    def test_check_win(self):
        # sudoku check win necesita de tenir la matriu inicialitzada
        # no s'ha implementat un mock object per fer aixo ja que la matriu esta formada per objectes square no per numeros
        # aixo fa que la implementacio d'un mock object sigui bastant complexa 
        # i s'ha cregut mes convenient cridar a la funcio mapFromFile que propociona un sudocku correcte
        sudoku_test = sudoku()
        sudoku_test.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/saved.txt")
        self.assertFalse(sudoku_test.checkWin())
        sudoku_completed = sudoku()
        sudoku_completed.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/completed.txt")
        self.assertTrue(sudoku_completed.checkWin())

    def test_check_number(self):
        # sudoku check number necesita de tenir la matriu inicialitzada
        # no s'ha implementat un mock object per fer aixo ja que la matriu esta formada per objectes square no per numeros
        # aixo fa que la implementacio d'un mock object sigui bastant complexa 
        # i s'ha cregut mes convenient cridar a la funcio mapFromFile que propociona un sudocku correcte
        sudoku_test = sudoku()
        sudoku_test.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/saved.txt")
        # aquesta funcio es troba dintre de addNumber, per tant ja esta comprobat que els numeros que li arribaran son [1,9]
        # nomes comprobem si fa be la seva funcio utilitzant el mapa predefinit
        self.assertFalse(sudoku_test.checkNum(1,1,1))
        self.assertFalse(sudoku_test.checkNum(2,1,1))
        self.assertFalse(sudoku_test.checkNum(3,1,1))
        self.assertTrue(sudoku_test.checkNum(4,1,1)) #valid
        self.assertTrue(sudoku_test.checkNum(5,1,1)) #valid
        self.assertFalse(sudoku_test.checkNum(6,1,1))
        self.assertFalse(sudoku_test.checkNum(7,1,1))
        self.assertFalse(sudoku_test.checkNum(8,1,1))
        self.assertFalse(sudoku_test.checkNum(9,1,1))


    def test_condition_and_decision_and_path_coverage_add_number(self):
        sudoku_test = sudoku()
        sudoku_test.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/saved.txt")
        # comprovacio del numero
        self.assertFalse(sudoku_test.addNumber(0,1,1)) #num<1 true num>9 false-> True
        self.assertFalse(sudoku_test.addNumber(10,1,1)) #num<1 false num>9 true -> True
        self.assertTrue(sudoku_test.addNumber(4,1,1)) #num<1 false num>9 false -> False (numero Valid)
        # comprovacio de columna
        self.assertFalse(sudoku_test.addNumber(4,0,1)) #num<1 true num>9 false-> True
        self.assertFalse(sudoku_test.addNumber(4,10,1)) #num<1 false num>9 true -> True
        self.assertFalse(sudoku_test.addNumber(1,1,1)) #num<1 false num>9 false -> False (numero no Valid)
        # comprovacio de fila
        self.assertFalse(sudoku_test.addNumber(1,1,0)) #num<1 true num>9 false-> True
        self.assertFalse(sudoku_test.addNumber(1,1,10)) #num<1 false num>9 true -> True
        self.assertFalse(sudoku_test.addNumber(1,1,1)) #num<1 false num>9 false -> False (numero no Valid)
        
    def test_condition_and_decision_and_path_coverage_check_win(self):
        # comprovacio de mapa amb zeros
        sudoku_test = sudoku()
        sudoku_test.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/saved.txt")
        self.assertFalse(sudoku_test.checkWin()) # -> False
        # comprovacio de mapa sense zeros
        sudoku_completed = sudoku()
        sudoku_completed.mapFromFile("/home/ivan/Desktop/TQS_pract/maps/completed.txt")
        self.assertTrue(sudoku_completed.checkWin()) # -> True

    def test_condition_and_decision_and_path_coverage_select_dificulty(self):
        sudoku_test = sudoku()
        self.assertTrue(sudoku_test.selectDificulty(1)) # -> True False False False
        self.assertTrue(sudoku_test.selectDificulty(3)) # -> False True False False
        self.assertTrue(sudoku_test.selectDificulty(2)) # -> False False True False
        self.assertFalse(sudoku_test.selectDificulty(0)) # -> False False False True
        

if __name__ == '__main__':
    unittest.main()