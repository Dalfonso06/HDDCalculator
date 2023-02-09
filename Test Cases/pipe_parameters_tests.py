import sys
sys.path.append('/Users/danielalfonso/Desktop/HDD Calculator')

import unittest
from Calculations import pipe_parameters

class TestPipeParameters(unittest.TestCase):

    # Pipe Parameters Test Cases
    def test_t(self):
        outside_diameter = 30
        dimension_ratio = 10
        expected = 3
        result = pipe_parameters.PipeParameters.t(outside_diameter, dimension_ratio)
        self.assertEqual(result, expected)

    def test_AOS(self):
        outside_diameter = 30
        expected = 706.86
        result = round(pipe_parameters.PipeParameters.AOS(outside_diameter), 2)
        self.assertEqual(result, expected)

    def test_AIS(self):
        inside_diameter = 24.218
        expected = 460.65
        result = round(pipe_parameters.PipeParameters.AIS(inside_diameter), 2)
        self.assertEqual(result, expected)

    def test_ACS(self):
        outside_diameter = 30
        inside_diameter = 24.218
        expected = 246.21
        result = round(pipe_parameters.PipeParameters.ACS(outside_diameter, inside_diameter), 2)
        self.assertEqual(result, expected)

    def test_ATL(self):
        outside_diameter = 30
        inside_diameter = 24.218
        safe_pull_stress = 1150
        expected = 283145.26
        result = round(pipe_parameters.PipeParameters.ATL(safe_pull_stress, outside_diameter, inside_diameter), 2)


if __name__ == "__main__":
    unittest.main()