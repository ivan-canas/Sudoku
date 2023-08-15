import unittest
import sys
sys.path.insert(1, '/home/ivan/Desktop/TQS_pract')
from square import square

class TestSquareMethods(unittest.TestCase):
    def test_get_num(self):
        square_test = square(False,1)
        self.assertEquals(square_test.getNum(),1)
        square_test = square(False,5)
        self.assertEquals(square_test.getNum(),5)
        square_test = square(False,9)
        self.assertEquals(square_test.getNum(),9)
    
    def test_set_num(self):
        square_test = square(False,5)
        # valors frontera
        self.assertTrue(square_test.setNum(1))
        self.assertTrue(square_test.setNum(9))
        # valors interns frontera
        self.assertTrue(square_test.setNum(2))
        self.assertTrue(square_test.setNum(8))
        # valors externs frontera
        self.assertFalse(square_test.setNum(0))
        self.assertFalse(square_test.setNum(10))

    def test_get_type(self):
        square_test = square(False,1)
        self.assertEquals(square_test.getType(),False)
        square_test = square(True,1)
        self.assertEquals(square_test.getType(),True)
        square_test = square(False,1)
        self.assertEquals(square_test.getType(),False)
    def test_set_type(self):
        square_test = square(False,5)
        # valors possibles
        self.assertTrue(square_test.setType(True))
        self.assertTrue(square_test.setType(False))
        # valors no possibles
        self.assertFalse(square_test.setType(1))
        self.assertFalse(square_test.setType('hola'))

if __name__ == '__main__':
    unittest.main()