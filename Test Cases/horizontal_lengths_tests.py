import sys
sys.path.append('/Users/danielalfonso/Desktop/HDD Calculator')

import unittest
from Calculations import horizontal_lengths

class TestHorizontalLengths(unittest.TestCase):
    
    def test_length_of_path(self):
        # Setup
        h_length_test = horizontal_lengths.HorizontalLenghts()
        h_lengths = [50.00, 489.22, 562.81, 512.85]
        
        # Calculate
        expected = 1614.88
        result = h_length_test.length_of_path(h_lengths)

        # Assert
        self.assertEqual(result, expected)

    def test_borehold_diameter(self):
        # Setup
        h_length_test = horizontal_lengths.HorizontalLenghts()
        outside_diameter1 = 30
        outside_diameter2 = 20

        # Calculate
        expected1 = 42.0
        expected2 = 30.0
        result1 = h_length_test.borehole_diameter(outside_diameter1)
        result2 = h_length_test.borehole_diameter(outside_diameter2)
        
        # Assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)

if __name__ == "__main__":
    unittest.main()