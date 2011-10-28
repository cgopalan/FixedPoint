import unittest
from fixedpoint import AFixedPoint

class AFixedPointTest(unittest.TestCase):
    '''Tests for the FixedPoint class '''
    def test_positiveint(self):
        self.assertEqual(float(AFixedPoint(2.0)), 2.0)
        
    def test_positivefloat(self):
        self.assertEqual(float(AFixedPoint(3.14)), 3.14)
        
    def test_negativeint(self):
        self.assertEqual(float(AFixedPoint(-1.0)), -1.0)
        
    def test_negativefloat(self):
        self.assertEqual(float(AFixedPoint(-2.5)), -2.5)
        
    def test_positivehex(self):
        self.assertEqual(float(AFixedPoint("0x00327eb8")), 100.99)
        
    def test_negativehex(self):
        self.assertEqual(float(AFixedPoint("0x80014000")), -2.5)
        
if __name__ == '__main__':
    unittest.main()