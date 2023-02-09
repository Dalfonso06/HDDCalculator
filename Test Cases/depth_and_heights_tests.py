import sys
sys.path.append('/Users/danielalfonso/Desktop/HDD Calculator/Calculations')

import unittest
import depth_and_heights, elevations

class TestDepthAndHeights(unittest.TestCase):
    
    def test_hpoint_a(self):
        # Setup
        elevations_test = elevations.Elevations(680.00, 704.00, 625.00, 663.00, 676.00, 685.00)
        outside_diameter = 30
        depth_test = depth_and_heights.DepthAndHeights(elevations_test, outside_diameter)

        # Calculate
        expected = 53.75
        result = round(depth_test.hpoint_a(), 2)

        # Assert
        self.assertEqual(result, expected)

    def test_hpoint_b(self):
        # Setup
        elevations_test = elevations.Elevations(680.00, 704.00, 625.00, 663.00, 676.00, 685.00)
        outside_diameter = 30
        depth_test = depth_and_heights.DepthAndHeights(elevations_test, outside_diameter)

        # Calculate
        expected = 77.75
        result = round(depth_test.hpoint_b(), 2)

        # Assert
        self.assertEqual(result, expected)

    def test_hc_min(self):
        # Setup
        elevations_test = elevations.Elevations(680.00, 704.00, 625.00, 663.00, 676.00, 685.00)
        outside_diameter = 30
        depth_test = depth_and_heights.DepthAndHeights(elevations_test, outside_diameter)

        # Calculate
        expected = 36.75
        result = round(depth_test.hc_min(), 2)

        # Assert
        self.assertEqual(result, expected)

    def test_hc_max(self):
        # Setup
        elevations_test = elevations.Elevations(680.00, 704.00, 625.00, 663.00, 676.00, 685.00)
        outside_diameter = 30
        depth_test = depth_and_heights.DepthAndHeights(elevations_test, outside_diameter)

        # Calculate
        expected = 58.75
        result = round(depth_test.hc_max(), 2)

        # Assert
        self.assertEqual(result, expected)

    def test_hw(self):
        # Setup
        elevations_test = elevations.Elevations(680.00, 704.00, 625.00, 663.00, 676.00, 685.00)
        outside_diameter = 30
        depth_test = depth_and_heights.DepthAndHeights(elevations_test, outside_diameter)

        # Calculate
        expected = 49.75
        result = round(depth_test.hw(), 2)

        # Assert
        self.assertEqual(result, expected)
        

if __name__ == "__main__":
    unittest.main()