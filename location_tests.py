import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

        """More test cases"""
        loc1= Location ("SLO", 35.3,-120.7)
        self.assertEqual(loc==loc1, True)

        loc2=Location("Vietnam", 14.1,108.3)
        self.assertEqual(repr(loc2),"Location('Vietnam', 14.1, 108.3)")

if __name__ == "__main__":
        unittest.main()
