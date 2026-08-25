import unittest

from solution import length_of_lis


class TestLongestIncreasingSubsequence(unittest.TestCase):

    # Random input test 1
    def test_example_one(self):
        self.assertEqual(length_of_lis([1,3,5,2,4]), 3)

    # Random input test 2
    def test_example_two(self):
        self.assertEqual(length_of_lis([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1]), 8)

    # What if the input is empty? 
    def test_empty(self):
        self.assertEqual(length_of_lis([]), 0)

    # Does the function know input can have 1 element?
    def test_single_element(self):
        self.assertEqual(length_of_lis([7]), 1)

    # What if every element in input is the same? 
    def test_all_equal(self):
        self.assertEqual(length_of_lis([1,1,1,1,1]), 1)

    # What if every number is bigger than the previous? 
    def test_strictly_increasing(self):
        self.assertEqual(length_of_lis([1,2,3,4,5,6,7,8,9]), 9)

    # What if every number is smaller than the previous? 
    def test_strictly_decreasing(self):
        self.assertEqual(length_of_lis([9,8,7,6,5,4,3,2,1]), 1)


if __name__ == "__main__":
    unittest.main()