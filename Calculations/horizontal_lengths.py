import math

class HorizontalLenghts:
    """Calculates the horizontal lengths (H_Length) Section 2.6."""

    @staticmethod
    def length_of_path(lengths: list):
        """Calculate the total length of H_Length.

        Args:
            lengths (list): All the lengths of the H_Length in feet.

        Returns:
            float: The total H_Length in feet.
        """
        return math.fsum(lengths)

    @staticmethod
    def borehole_diameter(outside_diameter: float):
        """Calculates the D hole or borehole diameter.

        Args:
            outside_diameter (float): Outside diameter of pipe in inches.

        Returns:
            float: Borehole diameter in inches
        """
        if outside_diameter < 24.0:
            return outside_diameter * 1.5
        else:
            return outside_diameter + 12