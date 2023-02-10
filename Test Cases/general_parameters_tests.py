import sys
sys.path.append('/Users/danielalfonso/Desktop/HDD Calculator/Calculations')

import unittest
import general_parameters, pipe_parameters


class TestGeneralParemeters(unittest.TestCase):
    
    def test_empty_pipe_weight(self):
        # Setup
        gp_test = general_parameters.GeneralParameters()
        outside_diameter = 30
        inside_diameter = 24.218
        specific_gravity = 0.95

        # Calculate
        expected = 101.40
        result = round(gp_test.empty_pipe_weight(outside_diameter, inside_diameter, specific_gravity), 2)

        # Assert
        self.assertEqual(result, expected)

    def test_filled_pipe_weight(self):
        # Setup
        gp_test = general_parameters.GeneralParameters()
        outside_diameter = 30
        inside_diameter = 24.218
        specific_gravity = 0.95
        empty_pipe = gp_test.empty_pipe_weight(outside_diameter, inside_diameter, specific_gravity)
        to_fill = 1
        Yib = 1

        # Calculate
        expected = 301.11
        result = round(gp_test.filled_pipe_weight(empty_pipe, to_fill, Yib, inside_diameter), 2)

        # Assert
        self.assertEqual(result, expected)

    def test_upward_buoyant_force(self):
        # Setup
        gp_test = general_parameters.GeneralParameters()
        outside_diameter = 30
        inside_diameter = 24.218
        specific_gravity = 0.95
        empty_pipe = gp_test.empty_pipe_weight(outside_diameter, inside_diameter, specific_gravity)
        to_fill = 1
        Yib = 1
        filled_pipe = gp_test.filled_pipe_weight(empty_pipe, to_fill, Yib, inside_diameter)
        Yb = 1.139

        # Calculate
        expected = 47.93
        result = round(gp_test.upward_buoyant_force(filled_pipe, outside_diameter, Yb), 2)

        # Assert
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()