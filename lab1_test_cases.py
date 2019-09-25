import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Test when the list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        """More test cases"""
        self.assertEqual(max_list_iter([3,5,7,13,10,5]),13)
        self.assertEqual(max_list_iter([-2,-3,3.5,4.7]),4.7)
        

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        """More test cases"""
        self.assertEqual(reverse_rec([1.2,2.3,4.6]),[4.6,2.3,1.2])

    def test_bin_search(self):
        """Test when the list has nonnegative intergers"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None)

        """Test when the list has negative intergers"""
        list_val =[-6,-4,-3,2,5]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-3, 0, len(list_val)-1, list_val), 2 )
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), None )

        """Test when the list has floats"""
        list_val =[-2.4,-1.2,0,3.5,5,6]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-1.2, 0, len(list_val)-1, list_val), 1 )
        self.assertEqual(bin_search(3.5, 0, len(list_val)-1, list_val), 3 )
        self.assertEqual(bin_search(-4, 0, len(list_val)-1, list_val), None )

        """Test when the list has repeated items"""
        list_val =[-2,0,0.1,0.2,0.2]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0.2, 0, len(list_val)-1, list_val), 3 )

                
        """Test when the list has 1 item"""        
        list_val =[1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), None )

        """Test when the list has no item"""
        list_val =[]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), None )
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None )

        
        

if __name__ == "__main__":
        unittest.main()

    
