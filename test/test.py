from split_array import split
import unittest


class TestSplitArray(unittest.TestCase):

    def test_reminder(self):
        new_array = split([1,2,3,4,5,6,7],2);
        self.assertEqual(new_array.splitter_operator, [[1, 2], [3, 4], [5, 6], [7]])
        
    def test_even_split(self):
        new_array = split([1,2,3,4,5,6],3);
        self.assertEqual(new_array.splitter_operator, [[1, 2, 3], [4, 5, 6]])
        
    def test_empty_list(self):
        new_array = split([],2);
        self.assertEqual(new_array.splitter_operator, [])
    
    def test_wrong_splitter_type(self):
        with self.assertRaises(TypeError):
            split([], 'a')
    
    def test_non_postive_splitter(self):
        with self.assertRaises(ValueError):
            split([1,2,3,4,5,6,7],-2);
    
    def test_non_integer(self):
        with self.assertRaises(TypeError):
            split([1,2,3,4,5,6,7],1.1);
    
    def test_non_list(self):
        with self.assertRaises(TypeError):
            split(str(1,2,3,4,5,6,7),1.1);
            
            
if __name__ == '__main__':
    unittest.main()