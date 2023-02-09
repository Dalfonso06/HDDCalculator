import sys
sys.path.append('/Users/danielalfonso/Desktop/HDD Calculator')

import unittest
from Calculations import curvature

class CurvatureTest(unittest.TestCase):

    # Curvature Test Cases
    def test_curvature_angle_radians(self):
        # Setup
        test_instance = curvature.Curvature(True, 1000, 404)
        expected = 0.404
        result = round(test_instance.curvature_angle_radians(), 3)

        # Assert
        self.assertEqual(result, expected)

        # Setup - no curvature
        test_instance_no_curve = curvature.Curvature(False, 1000, 404)
        expected = 0
        result = round(test_instance_no_curve.curvature_angle_radians(), 3)

        # Assert
        self.assertEqual(result, expected)

    def test_curvature_angle_degrees(self):
        # Setup
        test_instance = curvature.Curvature(True, 1000, 404)
        expected = 23.15
        result = round(test_instance.curvature_angle_degrees(), 2)

        # Assert
        self.assertEqual(result, expected)

        # Setup - no curvature
        test_instance_no_curve = curvature.Curvature(False, 1000, 404)
        expected = 0
        result = round(test_instance_no_curve.curvature_angle_degrees(), 2)

        # Assert
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

