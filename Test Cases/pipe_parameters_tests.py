import sys
sys.path.append('/Users/danielalfonso/Desktop/HDD Calculator')

import unittest
from Calculations import pipe_parameters

class TestPipeParameters(unittest.TestCase):

    # Pipe Parameters Test Cases
    def test_t(self):
        # Setup
        current_pipe = pipe_parameters.PipeParameters()
        outside_diameter = 30
        dimension_ratio = 10

        # Calculate
        expected = 3
        result = current_pipe.t(outside_diameter, dimension_ratio)

        # Assert
        self.assertEqual(result, expected)

    def test_AOS(self):
        # Setup
        current_pipe = pipe_parameters.PipeParameters()
        outside_diameter = 30

        # Calculate
        expected = 706.86
        result = round(current_pipe.AOS(outside_diameter), 2)

        # Assert
        self.assertEqual(result, expected)

    def test_AIS(self):
        # Setup
        current_pipe = pipe_parameters.PipeParameters()
        inside_diameter = 24.218

        # Calculate
        expected = 460.65
        result = round(current_pipe.AIS(inside_diameter), 2)

        # Assert
        self.assertEqual(result, expected)

    def test_ACS(self):
        # Setup
        current_pipe = pipe_parameters.PipeParameters()
        outside_diameter = 30
        inside_diameter = 24.218

        # Calculate
        expected = 246.21
        result = round(current_pipe.ACS(outside_diameter, inside_diameter), 2)

        # Assert
        self.assertEqual(result, expected)

    def test_ATL(self):
        # Setup
        current_pipe = pipe_parameters.PipeParameters()
        outside_diameter = 30
        inside_diameter = 24.218
        safe_pull_stress = 1150

        # Calculate
        expected = 283145.26
        result = round(current_pipe.ATL(safe_pull_stress, outside_diameter, inside_diameter), 2)

        # Assert
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()