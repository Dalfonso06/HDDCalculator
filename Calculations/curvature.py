import math

# 2 --------------- Path Parameters ---------------
class Curvature:
    """Class for Curvature Section 2.3 A and B."""

    def __init__(self, horizontal_curve: bool, radius_of_curve: float, length_of_curve: float):
        """Instance method for curvature function (horizontal or compound)

        Args:
            horizontal_curve (bool): Determine if there is a curve.
            radius_of_curve (float): Radius in feet.
            length_of_curve (float): Length in feet.
        """
        self.horizontal_curve = horizontal_curve
        self.radius_of_curve = radius_of_curve
        self.length_of_curve = length_of_curve

    def curvature_angle_radians(self):
        """Calculate the curvature angle

        Returns:
            float: Curvature angle in radians.
        """
        if (self.horizontal_curve):
            return self.length_of_curve / self.radius_of_curve
        else:
            return 0.0

    def curvature_angle_degrees(self):
        """Calculate the curvature angle

        Returns:
            float: Curvature angle in degrees.
        """
        pi = math.pi
        if (self.horizontal_curve):
            return self.curvature_angle_radians() * (180/pi)
        else:
            return 0.0