import unittest
from unittest.mock import MagicMock, Mock
import numpy as np
import sys
sys.path.insert(1, '/home/ivan/Desktop/TQS_pract')
from sudokuGenerator import sudokuGenerator
from square import square

class TestSudokuGeneratorMethods(unittest.TestCase):
    def test_remove_some(self):
        # comprobem si el numero de caselles tretes coincideix amb el nivell de dificultat
        mock = Mock(return_value=1)
        sudokuGenerator_test = sudokuGenerator(mock())
        matrix = np.ones(shape=(9,9))
        m, diff = sudokuGenerator_test.remove_some(matrix)
        self.assertGreaterEqual(diff,12)
        self.assertLessEqual(diff,15)
        sudokuGenerator_test = sudokuGenerator(2)
        matrix = np.ones(shape=(9,9))
        m, diff = sudokuGenerator_test.remove_some(matrix)
        self.assertGreaterEqual(diff,15)
        self.assertLessEqual(diff,19)
        sudokuGenerator_test = sudokuGenerator(3)
        matrix = np.ones(shape=(9,9))
        m, diff = sudokuGenerator_test.remove_some(matrix)
        self.assertGreaterEqual(diff,19)
        self.assertLessEqual(diff,23)

    def test_generate_matrix(self):
        # comprobem que la matriu resultant generada aleatoriament es valida
        sudokuGenerator_test = sudokuGenerator(1)
        self.assertTrue(sudokuGenerator_test.generateMatrix())

    

if __name__ == '__main__':
    unittest.main()